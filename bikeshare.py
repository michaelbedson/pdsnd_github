import input as inp
import main as mn


def main():
    while True:
        city, month, day = mn.get_filters()
        df = mn.load_data(city, month, day)

        mn.time_stats(df)
        mn.station_stats(df)
        mn.trip_duration_stats(df)
        mn.user_stats(df)
        inp.get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no. __ ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
