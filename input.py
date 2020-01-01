def get_input(user_input, data_list):
    # take user input and converting to lowercase
    # check if user entered correct data
    while True:
        user_data = input(user_input).lower()
        if user_data in data_list:
            return user_data
        else:
            print("\nenter the correct data asked")


def run_raw(df, raw_data, left, right):
    # displays the raw table based on users request
    raw_response = ['yes', 'no']
    while raw_data == 'yes':
        print(df.iloc[left:right])
        left += 5
        right += 5
        raw_data = input("\nWould you like to see 5 more sample raw data? Type yes or no:__ ").lower()
        while raw_data not in raw_response:
            raw_data = input("\nPlease enter yes or no:__ ")


def get_raw_data(df):
    # takes users input for displaying raw data
    raw_response = ['yes', 'no']
    raw_data = input("\nWould you like to see new 5 line sample raw data? Type yes or no:__ ").lower()
    left = 0
    right = 5
    if raw_data not in raw_response:
        raw_data = input("\nPlease enter yes or no:__ ")
        while raw_data not in raw_response:
            raw_data = input("\nPlease enter yes or no:__ ")
        run_raw(df, raw_data, left, right)
    else:
        run_raw(df, raw_data, left, right)