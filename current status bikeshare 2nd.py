# udacity-git-project: adding a comment to use it for a further commit

import time
import pandas as pd
import numpy as np

def print_pause(text_to_print, delay=0):
    print(text_to_print)
    time.sleep(delay)
# function to add some time delay


def intro():
    print_pause("In this program you explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington.", 3)
    print_pause("According to your input the program will provide information by computing descriptive statistics.", 3)
# function to add introduction

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

answers = ['yes', 'no']

def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')

# function to get valid input with the arguments prompt for the question and options for the valid answers

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = str(valid_input("Which city? Chicago, New York City or Washington?\n", cities))
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(valid_input("Which month? Choose between January and June or all?\n", months))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(valid_input("Which day? Choose between Monday to Sunday or all?\n", days))

    print('-'*40)
    return city, month, day


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday
    popular_day = df['weekday'].mode()[0]
    print('Most Popular Start Day:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['track'] = df['Start Station'] + df['End Station']
    popular_track = df['track'].mode()[0]
    print('Most Frequent Track:', popular_track)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_time)


    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', avg_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()

        latest_birth = df['Birth Year'].max()

        common_year = df['Birth Year'].mode()

        print('Earliest, most recent, most common year of birth:', earliest_birth, latest_birth, common_year )
    else:
        print('Unfortunately there is no data of gender or year of birth to display.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_stats(df):
    """Displays 5 rows of raw data upon request by the user."""
    current_line = 0
    while True:
        display = str(valid_input("Would you like to see raw data? Enter yes or no.\n", answers))
        if display.lower() == 'yes':
            print(df.iloc[current_line:current_line+5])
            current_line += 5
        if display.lower() != 'yes':
            break


def main():
    intro()
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
