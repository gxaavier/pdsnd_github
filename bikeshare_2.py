#!/usr/bin/env python
# coding: utf-8

# In[33]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[34]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Do you want to see data for Chicago, New York City or Washington?\n')
        if city.lower() == 'chicago':
            city = 'chicago'
        elif city.lower() == 'new york city':
            city = 'new york city'
        elif city.lower() == 'washington':
            city = 'washington'
        else:
            print('Sorry, your input must be either Chicago, New York City or Washington.')
    # get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Do you want to filter your data by month? Please type a month between Jan and June or type "all" to not filter.\n')
        if month.lower() == 'january':
            month = 'january'
        elif month.lower() == 'february':
            month = 'february'
        elif month.lower() == 'march':
            month = 'march'
        elif month.lower() == 'april':
            month = 'april'
        elif month.lower() == 'may':
            month = 'may'
        elif month.lower() == 'june':
            month = 'june'
        elif month.lower() == 'all':
            month = 'all'
        else:
            print('Sorry, your input must be a month between January and June or "all" to not filter by any month.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Do you want to filter your data by day? Please type a day between Sunday and Monday or type "all" to not filter.\n')
        if day.lower() == 'monday':
            day = 'monday'
        elif day.lower() == 'tuesday':
            day = 'tuesday'
        elif day.lower() == 'wednesday':
            day = 'wednesday'
        elif day.lower() == 'thursday':
            day = 'thursday'
        elif day.lower() == 'friday':
            day = 'friday'
        elif day.lower() == 'saturday':
            day = 'saturday'
        elif day.lower() == 'sunday':
            day = 'sunday'
        elif day.lower() == 'all':
            day = 'all'
        else:
            print('Sorry, your input must be a day between Sunday and Monday or "all" to not filter by any day.')

    print('-'*60)


    return city, month, day


# In[35]:


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
    # Loading CSV file from city input
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')
    # Changing datatype to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Creating two new columns to show month and day from Start Time column
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.weekday_name
    # Filtering by month and day that are already known by user input
    if month != 'all' and day != 'all':
        df = df[(df['Month'] == month.title()) & (df['Day'] == day.title())]
    elif month == 'all' and day != 'all':
        df = df[df['Day'] == day.title()]
    elif month != 'all' and day == 'all':
        df = df[df['Month'] == month.title()]
    elif month == 'all' and day == 'all':
        df = df


    return df


# In[36]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['Month'].mode()[0]
    print('The most common month is: {}'.format(popular_month))

    # display the most common day of week
    popular_day = df['Day'].mode()[0]
    print('The most common day is: {}'.format(popular_day))

    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[37]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_st_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(popular_st_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'].str.cat(df['End Station'], sep= ' to ').mode()[0]
    print('The most frequent trip is: {}'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[38]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # Changing times to TimeDeltas
    # df['Start Time'] = pd.to_timedelta(df['Start Time'])
    # df['End Time'] = pd.to_datetime(df['End Time'])
    # df['End Time'] = pd.to_timedelta(df['End Time'])
    # Creating trip duration
    # df['Trip Duration'] = df['End Time'] - df['Start Time']
    total_trip_dur = round(((df['Trip Duration'].sum())/3600)/24, 2)
    print('The total trip duration was: {} days'.format(total_trip_dur))

    # display mean travel time
    mean_trip_dur = round((df['Trip Duration'].mean())/60, 2)
    print('The mean trip duration was: {} minutes'.format(mean_trip_dur))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[39]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    sub = df.groupby('User Type').count()['Day']['Subscriber']
    cust = df.groupby('User Type').count()['Day']['Customer']
    if 'Dependent' in df['User Type'].unique():
        dep = df.groupby('User Type').count()['Day']['Dependent']
        print('''The User Types counts are:\n
             Subscriber: {}\n
             Customer: {}\n
             Dependent: {}'''.format(sub, cust, dep))
    else:
         print('''The User Types counts are:\n
             Subscriber: {}\n
             Customer: {}\n'''.format(sub, cust))

    # Display counts of gender
    if 'Gender' in df.columns:
        male = df.groupby('Gender').count()['Day']['Male']
        female = df.groupby('Gender').count()['Day']['Female']
        print('''The Gender counts are:\n
                 Male: {}\n
                 Female: {}\n'''.format(male, female))
    else:
        print('Gender information is not present in data.\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].sort_values().max())
        most_recent = int(df['Birth Year'].sort_values().min())
        most_common = int(df['Birth Year'].sort_values().mode()[0])
        print('''The earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is: {}'''
              .format(earliest, most_recent, most_common))
    else:
        print('Birth Year information is not present in data.\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[40]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
