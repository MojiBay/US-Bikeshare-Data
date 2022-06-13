import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # why we did not use the same while loop as the one for month?
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter one of these cities : "chicago", "new york city", "washington" : ').lower()
    while city not in CITY_DATA:
        print('Please enter the name correctly.')
        city = input('Please enter one of these cities : "chicago", "new york city", "washington" : ').lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    while True:
        month = input('Please enter one of these months: "january", "february", "march", "april", "may", "june", "all" : ').lower()
        if month in months:
            break
        else:
          print('Please, enter the name correctly!')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while True:
        day = input('Please enter one of these days : "sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all" : ').lower()
        if day in days:
            break
        else:
          print('Please, enter the name correctly!')


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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_the_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the busiest month is : {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('the busiest day of week is : {}'.format(df['day_of_the_week'].mode()[0]))

    # display the most common start hour
    print('the busiest start hour is : {}'.format(df['start hour'].mode()[0]))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most popular end station is: {}'.format(df['End Station'].mode()[0]))

     # display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+","+df['End Station']
    print('The most popular route is: {}'.format(df['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time : ',(df['Trip Duration'].sum().round()))

    # display mean travel time
    print('Total travel time : ',(df['Trip Duration'].mean().round()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city != 'washington':
      print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
      print('The most earliest year of birth is : ',int(df['Birth Year'].min()))
      print('The most recent year of birth is : ',int(df['Birth Year'].max()))
      print('The most common year of birth is : ',int(df['Birth Year'].mode()[0]))
    else:
        print('No data has been submitted for washington')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('The raw data display...')
    index=0
    input_data=input('Do you like to see 5 rows of first data? Enter "yes" or "no"  ').lower()
    if input_data not in ['yes','no']:
        print('Please enter a valid answer between "yes" or "no')
        input_data=input('Do you like to see 5 rows of first data? Enter "yes" or "no"').lower()
    elif input_data != 'yes':
         print('Okay. Bye!')

    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index += 5
            input_data=input('Do you like to see 5 more rows of the raw data? Enter "yes" or "no"').lower()
            if input_data !="yes":
                print('Okay.Bye!')
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Bye!')
            break


if __name__ == "__main__":
	main()
