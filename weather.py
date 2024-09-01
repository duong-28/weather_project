import csv
from datetime import datetime
from pprint import pprint

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"
# print(format_temperature(5))

def convert_date(iso_string):
    """Converts an into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # ISO String: YYYYMMDD or YYYY-MM-DD
    # Convert iso_string into an object
    date_object = datetime.fromisoformat(iso_string) #this includes date and time
    # define the readable format
    readable_format = "%A %d %B %Y"
    converted_date = datetime.strftime(date_object,readable_format)
    return converted_date

# print(convert_date("2021-10-31T07:00:00+08:00"))

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_cel = (float(temp_in_fahrenheit) - 32) * 5/9
    return round(temp_in_cel,1)

# print(convert_f_to_c(100.00))

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Solution 1: 
    # list = [] 
    # for num in weather_data:
    #     list.append(float(num))
    # total = sum(list)
    # return total / len(weather_data)

    # Solution 2:
    total_value = 0 
    for num in weather_data:
        total_value += float(num)
    mean_value = total_value / len(weather_data)
    return mean_value

# print(calculate_mean(["51", "58", "59", "52", "52", "48", "47", "53"]))

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open (csv_file, 'r') as csv_file: 
        reader = csv.reader(csv_file)
        next(reader) #skipping the header in the csv file 
        data_list = []
        for row in reader:
            if row != []:
                date = row[0]
                min_value = int(row[1])
                max_value = int(row[2])
                data_list.append([date,min_value,max_value])
        return data_list

# print(load_data_from_csv("tests/data/example_one.csv"))

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # Step 1: Find the min value in the weather data list - when length of list is zero, return nothing
    if len(weather_data) == 0: 
        return ()
    min_value = float(min(weather_data))
    # Step 2: Find the position of the min value
    min_value_position = 0
    for index, num in enumerate(weather_data):
        if min_value == float(num): #num needs to be converted into float/ int as some of the values can be strings
            min_value_position = index
    return (min_value, min_value_position)

# print(find_min(["49", "57", "56", "55", "53", "49"]))

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0: 
        return ()
    max_value = float(max(weather_data))
    max_value_position = 0
    for index, num in enumerate(weather_data):
        if max_value == float(num):
            max_value_position = index
    return (max_value, max_value_position) 

# print(find_max([58, 54, 43, 60, 43, 71]))

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Step 1: Count the number of days in the weather data list
    num_days = len(weather_data)

    # Step 2: Find the minimum value in the weather data list
    min_list = []
    for index in weather_data: 
        min_list.append(index[1])
    find_min(min_list)
    # Since find_min returns a tuple => you want to parse its value to manipulate the data
    min_value, min_position = find_min(min_list)
    # Convert min temp from f to c
    cel_min_temp = convert_f_to_c(min_value)
    # Convert iso date to readable date format
    min_date = convert_date(weather_data[min_position][0])
     # Calculate average low
    average_low = convert_f_to_c(calculate_mean(min_list))
    
    # Step 3: Repeat Step 2 but for maximum temp
    max_list = []
    for index in weather_data: 
        max_list.append(index[2])
    find_max(max_list)
    max_value, max_position = find_max(max_list)
    cel_max_temp = convert_f_to_c(max_value)
    max_date = convert_date(weather_data[max_position][0])
    average_high = convert_f_to_c(calculate_mean(max_list))

    # Step 4: Return expected result
    return f"{num_days} Day Overview\n  The lowest temperature will be {cel_min_temp}°C, and will occur on {min_date}.\n  The highest temperature will be {cel_max_temp}°C, and will occur on {max_date}.\n  The average low this week is {average_low}°C.\n  The average high this week is {average_high}°C.\n"

# print(generate_summary([
#             ["2020-06-19T07:00:00+08:00", -47, -46],
#             ["2020-06-20T07:00:00+08:00", -51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", -52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", -48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]))

# Expected Output
# 8 Day Overview
#   The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is -16.1°C.
#   The average high this week is 12.4°C.


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # daily_summaries = []
    # for list in weather_data:
    #     date_convert = convert_date(list[0])
    #     min_temp = convert_f_to_c(list[1])
    #     max_temp = convert_f_to_c(list[2])
    #     daily_summary = f"---- {date_convert} ----\n Minimum Temperature: {min_temp}°C\n Maximum Temperature: {max_temp}°C\n"
    #     daily_summaries.append(daily_summary)
    #     # print(daily_summary)
    # return daily_summaries

    daily_summaries = ""
    for list in weather_data:
        date_convert = convert_date(list[0])
        min_temp = convert_f_to_c(list[1])
        max_temp = convert_f_to_c(list[2])
        daily_summaries += (f"---- {date_convert} ----\n  Minimum Temperature: {min_temp}°C\n  Maximum Temperature: {max_temp}°C\n\n")
    return daily_summaries
  
# print(generate_daily_summary([
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]))

# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

# ---- Sunday 04 July 2021 ----
#   Minimum Temperature: 13.3°C
#   Maximum Temperature: 16.7°C

# ---- Monday 05 July 2021 ----
#   Minimum Temperature: 12.8°C
#   Maximum Temperature: 16.1°C

# ---- Tuesday 06 July 2021 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 16.7°C
