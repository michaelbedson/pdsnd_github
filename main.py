import time
import pandas as pd
import input as inp


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington)
    while True:
        city = inp.get_input('Please input the city name:- (chicago), or (new york city), or (washington):__ ',
                         ['chicago', 'new york city', 'washington'])
        if city in ['chicago', 'new york city', 'washington']:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = inp.get_input('\nWhich month? january, february, march, april, may, june, all?__ ',
                          ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                           'october', 'november', 'december', 'all'])
        try:
            month.index(month)
        except:
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = inp.get_input('\nWhich day? monday, tuesday, wednesday, thursday, friday, saturday, sunday, all?__ ',
                        ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'])
        try:
            day.index(day)
        except:
            continue
        else:
            break
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'}
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

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
    #print(df)
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('*' * 40)
    print('\n The most common month: {} \n'.format(df['month'].mode()))

    # TO DO: display the most common day of week
    print('\n The most common date of week: {} \n'.format(df['day_of_week'].mode()))

    # TO DO: display the most common start hour
    print('\n The most common start hour: {} \n'.format(df['start_hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df.head()

    # TO DO: display most commonly used start station
    print('\n The most commonly used start station: {} \n'.format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print('\n The most commonly used end station: {} \n'.format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + 'to' + df['End Station']
    print(
        '\n The most frequent combination of start station and end station trip: {} \n'.format(df['start_end'].mode()))
    print("\nThis took %s seconds." % (time.time() - start_time))


print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\n The total travel time: {} \n '.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\n The mean travel time: {} \n'.format(df['Trip Duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))


print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n The counts of user types: {} \n'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\n The counts of gender is:\n', gender)
    except:
        pass

    # Gender may not be a part of the data set (washington.csv)
    try:

        df_Gender_Type = df['Gender'].value_counts()
        # Display counts of gender
        print('\nGender:\n')
    except:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('\n The earliest birth is:  \n ', earliest)
        print('\n The most recent birth is: \n', recent)
        print('\n The most common year of  birth is: \n', common)
    except:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
