############################ Header ####################################
# Purpose of program Bikeshare.py:
# Implement local functions (e.g. get_filters, load_data, time_stats, etc.) 
# to get user input, load data, and display statistics per filter.
########################################################################

# Import the following: TIME module, PANDAS library, NUMPY library
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

########################################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #------------------------------------------------------------------------#    
    # 1. TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #------------------------------------------------------------------------#
    
    # Ask user to input name of the city (Chicago, New York City, Washington).
    city = input("Type the name of the city (Chicago, New York City, Washington): ")

    # Convert user input to lowercase. If input was uppercase or mix of upper and lowercase, this will convert all characters to lowercase.
    city = city.lower()

    # While loop for handling invalid inputs
    while city not in CITY_DATA:
        print("Warning, invalid input. Enter a valid city name.")
        city = input("Type the name of the city (Chicago, New York City, Washington): ")
        city = city.lower()
        
    # Print selected city
    print("You entered:", city)
    
    #------------------------------------------------------------------------#
    # 2. TO DO: get user input for month (all, january, february, ... , june)
    #------------------------------------------------------------------------#
    
    # Ask user to enter the month
    month = input("Type the name of the month (all, January, February, ..., June): ")

    # Convert user input to title case
    month = month.lower()

    # While loop for handling invalid inputs
    while month not in MONTH_DATA:
        print("Warning, invalid input. Enter valid month.")
        month = input("Type the name of the month (all, January, February, ..., June): ")
        month = month.lower()

    # Print selected month
    print("You entered:", month)
    

    #------------------------------------------------------------------------#
    # 3. TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #------------------------------------------------------------------------#
    
    # Ask user to enter the day of the week
    day = input("Enter the day of the week (all, Monday, Tuesday, ... Sunday): ")

    # Convert input to lowercase
    day = day.lower()

    # Check if input is valid
    while day.lower() not in DAY_DATA:
        _day = input("\n\nType the name of the day you want to analyse (E.g. all, Monday, Tuesday, Wednesdays, Thursday, Friday, Saturday, Sunday)\n")
        if _day.lower() in DAY_DATA:
            # We were able to get the name of the month
            day = _day.lower()
        else:
            # We were not able to get the name of the month so continue the loop
            print("Warning, invalid input. Enter one of the following: all, Monday, Tuesday, Wednesdays, Thursday, Friday, Saturday, Sunday.\n") 
    
    print('-'*40)
    
    # Return values entered by user
    return city, month, day

########################################################################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data for the specified city (Chicago, New York City, or Washington) into a DataFrame  
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    # Convert START TIME column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Get month, day of the week, and hour from the START TIME column
    df['Month'] = df['Start Time'].dt.month
    df['Day']   = df['Start Time'].dt.day_name()
    df['Hour']  = df['Start Time'].dt.hour
    
    # Filter DataFrame by month
    if month != 'all':
        month = month.lower()
        # Map month names to month numbers
        month_map = {
            'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june': 6}
        # Filter
        df = df[df['Month'] == month_map[month]]
    
    # Filter DataFrame by day of the week        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['Day'] == day.title()]
        
    return df

########################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert START TIME column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #------------------------------------------------------------------------#
    # 4. TO DO: display the most common month
    #------------------------------------------------------------------------#
    
    # Print most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month:', most_common_month)
    
    #------------------------------------------------------------------------#
    # 5.  TO DO: display the most common day of week
    #------------------------------------------------------------------------#
    
    # Print most common day of week
    most_common_day = df['Day'].mode()[0]
    print('Most Common Day of Week:', most_common_day)
    
    #------------------------------------------------------------------------#
    # 6. TO DO: display the most common start hour
    #------------------------------------------------------------------------#

    # Print most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
########################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 7. TO DO: display most commonly used start station
    #------------------------------------------------------------------------#
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ", most_common_start_station)

    #------------------------------------------------------------------------#
    # 8. TO DO: display most commonly used end station
    #------------------------------------------------------------------------#
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: ", most_common_end_station)
    
    #------------------------------------------------------------------------#    
    # 9. TO DO: display most frequent combination of start station and end station trip
    #------------------------------------------------------------------------#
    most_frequent_combo = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip is : ", most_frequent_combo.split("||"))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 10. TO DO: display total travel time
    #------------------------------------------------------------------------#
    tot_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", tot_travel_time)

    #------------------------------------------------------------------------#
    # 11. TO DO: display mean travel time
    #------------------------------------------------------------------------#
    mean_travel_time = round(df['Trip Duration'].mean(), 1)
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################################################################
def user_stats(df, city):
    """Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
        (str) city - name of the city to analyze  
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 12. TO DO: Display counts of user types
    #------------------------------------------------------------------------#
    user_type = df['User Type'].value_counts()
    print("Number of user types: \n" + str(user_type))
   
    # Restrict to Chicago and NYC, otherwise get error in log
    if city == 'Chicago' or city == 'New York City':  
        
        #------------------------------------------------------------------------#
        # 13. TO DO: Display counts of gender
        #------------------------------------------------------------------------#        
        gender = df['Gender'].value_counts()
        print("Counts of gender: \n" + str(gender))

        #------------------------------------------------------------------------#
        # 14. TO DO: Display earliest, most recent, and most common year of birth
        #------------------------------------------------------------------------#
        earliest_yob    = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: {}\n'.format(earliest_yob))
        print('Most recent year of birth: {}\n'.format(most_recent_yob))
        print('Most common year of birth: {}\n'.format(most_common_yob) )
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
########################################################################

# Raw data is displayed upon request by the user in the following manner:
# Script should prompt the user if they want to see 5 lines of raw data,
# Display that data if the answer is 'yes',
# Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
# Stop the program when the user says 'no' or there is no more raw data to display.

def show_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print(df.head())
    next = 0
    
    while True:
        show = input('\nDo you want to see the first 5 rows of raw data? Type yes or no.\n')
        if show.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


########################################################################
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # show_raw_data function is called directly inside the if statement
        show = input('\nDo you want to see the first 5 rows of raw data? Type yes or no.\n')
        if show.lower() == 'yes':
            show_raw_data(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
||||||| 9c57cea
=======
############################ Header ####################################
# Purpose of program Bikeshare.py:
# Implement local functions (e.g. get_filters, load_data, time_stats, etc.) 
# to get user input, load data, and display statistics per filter.
########################################################################

# Import the following: TIME module, DOCTEST module, TABULATE library, PANDAS library, NUMPY library
import time
import doctest
import tabulate
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

########################################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #------------------------------------------------------------------------#    
    # 1. TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #------------------------------------------------------------------------#
    
    # Ask user to input name of the city (Chicago, New York City, Washington).
    city = input("Type the name of the city (Chicago, New York City, Washington): ")

    # Convert user input to lowercase. If input was uppercase or mix of upper and lowercase, this will convert all characters to lowercase.
    city = city.lower()

    # While loop for handling invalid inputs
    while city not in CITY_DATA:
        print("Warning, invalid input. Enter a valid city name.")
        city = input("Type the name of the city (Chicago, New York City, Washington): ")
        city = city.lower()
        
    # Print selected city
    print("You entered:", city)
    
    #------------------------------------------------------------------------#
    # 2. TO DO: get user input for month (all, january, february, ... , june)
    #------------------------------------------------------------------------#
    
    # Ask user to enter the month
    month = input("Type the name of the month (all, January, February, ..., June): ")

    # Convert user input to title case
    month = month.lower()

    # While loop for handling invalid inputs
    while month not in MONTH_DATA:
        print("Warning, invalid input. Enter valid month.")
        month = input("Type the name of the month (all, January, February, ..., June): ")
        month = month.lower()

    # Print selected month
    print("You entered:", month)
    

    #------------------------------------------------------------------------#
    # 3. TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #------------------------------------------------------------------------#
    
    # Ask user to enter the day of the week
    day = input("Enter the day of the week (all, Monday, Tuesday, ... Sunday): ")

    # Convert input to lowercase
    day = day.lower()

    # Check if input is valid
    while day.lower() not in DAY_DATA:
        _day = input("\n\nType the name of the day you want to analyse (E.g. all, Monday, Tuesday, Wednesdays, Thursday, Friday, Saturday, Sunday)\n")
        if _day.lower() in DAY_DATA:
            # We were able to get the name of the month
            day = _day.lower()
        else:
            # We were not able to get the name of the month so continue the loop
            print("Warning, invalid input. Enter one of the following: all, Monday, Tuesday, Wednesdays, Thursday, Friday, Saturday, Sunday.\n") 
    
    print('-'*40)
    
    # Return values entered by user
    return city, month, day

# If get_filters function works as expected, doctest will print a success message.
doctest.testmod(verbose=True)

########################################################################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data for the specified city (Chicago, New York City, or Washington) into a DataFrame  
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    # Convert START TIME column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Get month, day of the week, and hour from the START TIME column
    df['Month'] = df['Start Time'].dt.month
    df['Day']   = df['Start Time'].dt.day_name()
    df['Hour']  = df['Start Time'].dt.hour
    
    # Filter DataFrame by month
    if month != 'all':
        month = month.lower()
        # Map month names to month numbers
        month_map = {
            'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june': 6}
        # Filter
        df = df[df['Month'] == month_map[month]]
    
    # Filter DataFrame by day of the week        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['Day'] == day.title()]
        
    return df

doctest.testmod(verbose=True)

########################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert START TIME column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #------------------------------------------------------------------------#
    # 4. TO DO: display the most common month
    #------------------------------------------------------------------------#
    
    # Print most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month:', most_common_month)
    
    #------------------------------------------------------------------------#
    # 5.  TO DO: display the most common day of week
    #------------------------------------------------------------------------#
    
    # Print most common day of week
    most_common_day = df['Day'].mode()[0]
    print('Most Common Day of Week:', most_common_day)
    
    #------------------------------------------------------------------------#
    # 6. TO DO: display the most common start hour
    #------------------------------------------------------------------------#

    # Print most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
doctest.testmod(verbose=True)
    
########################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 7. TO DO: display most commonly used start station
    #------------------------------------------------------------------------#
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ", most_common_start_station)

    #------------------------------------------------------------------------#
    # 8. TO DO: display most commonly used end station
    #------------------------------------------------------------------------#
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: ", most_common_end_station)
    
    #------------------------------------------------------------------------#    
    # 9. TO DO: display most frequent combination of start station and end station trip
    #------------------------------------------------------------------------#
    most_frequent_combo = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip is : ", most_frequent_combo.split("||"))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

doctest.testmod(verbose=True)

########################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
    """
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 10. TO DO: display total travel time
    #------------------------------------------------------------------------#
    tot_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", tot_travel_time)

    #------------------------------------------------------------------------#
    # 11. TO DO: display mean travel time
    #------------------------------------------------------------------------#
    mean_travel_time = round(df['Trip Duration'].mean(), 1)
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################################################################
def user_stats(df, city):
    """Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) df - Pandas DataFrame with city data filtered by month and day
        (str) city - name of the city to analyze  
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #------------------------------------------------------------------------#
    # 12. TO DO: Display counts of user types
    #------------------------------------------------------------------------#
    user_type = df['User Type'].value_counts()
    print("Number of user types: \n" + str(user_type))
   
    # Restrict to Chicago and NYC, otherwise get error in log
    if city == 'Chicago' or city == 'New York City':  
        
        #------------------------------------------------------------------------#
        # 13. TO DO: Display counts of gender
        #------------------------------------------------------------------------#        
        gender = df['Gender'].value_counts()
        print("Counts of gender: \n" + str(gender))

        #------------------------------------------------------------------------#
        # 14. TO DO: Display earliest, most recent, and most common year of birth
        #------------------------------------------------------------------------#
        earliest_yob    = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: {}\n'.format(earliest_yob))
        print('Most recent year of birth: {}\n'.format(most_recent_yob))
        print('Most common year of birth: {}\n'.format(most_common_yob) )
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

doctest.testmod(verbose=True)
    
########################################################################

# Raw data is displayed upon request by the user in the following manner:
# Script should prompt the user if they want to see 5 lines of raw data,
# Display that data if the answer is 'yes',
# Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
# Stop the program when the user says 'no' or there is no more raw data to display.

def show_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print(df.head())
    next = 0
    
   while True:
        show_data = input('\nDo you want to see the first 5 rows of raw data? Type yes or no.\n')
        if show_data.lower() != 'yes':
            break
    # Using library TABULATE, this ensures one can view all columns
    print(tabulate(df_default.iloc[np.arange(0+i, 5+i)], headers="keys"))
    i += 5

doctest.testmod(verbose=True)

########################################################################
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # show_raw_data function is called directly inside the if statement
        show = input('\nDo you want to see the first 5 rows of raw data? Type yes or no.\n')
        if show.lower() == 'yes':
            show_raw_data(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
