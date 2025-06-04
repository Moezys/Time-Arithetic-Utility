def add_time(start, duration, starting_day=None):
    # Helper list for day-of-week calculations:
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # 1. Parse the 'start' time into hours, minutes, and AM/PM
    time_part, period = start.split()
    start_hour_str, start_min_str = time_part.split(':')
    start_hour = int(start_hour_str)
    start_min = int(start_min_str)
    period = period.upper()

    # Convert start hour to 24-hour format (0–23) for easier arithmetic
    if period == 'PM' and start_hour != 12:
        start_hour_24 = start_hour + 12
    elif period == 'AM' and start_hour == 12:
        start_hour_24 = 0
    else:
        start_hour_24 = start_hour

    # 2. Parse the 'duration' into hours and minutes
    dur_hour_str, dur_min_str = duration.split(':')
    dur_hour = int(dur_hour_str)
    dur_min = int(dur_min_str)

    # 3. Add up minutes, then handle minute overflow
    total_minutes = start_min + dur_min
    extra_hours_from_minutes = total_minutes // 60
    result_min = total_minutes % 60

    # 4. Add hours (including any carried over from minutes)
    total_hours_24 = start_hour_24 + dur_hour + extra_hours_from_minutes

    # 5. Compute how many days have passed and the final hour in 24h
    days_passed = total_hours_24 // 24
    result_hour_24 = total_hours_24 % 24

    # 6. Convert result_hour_24 back to 12-hour format + AM/PM
    if result_hour_24 == 0:
        result_hour_12 = 12
        result_period = 'AM'
    elif 1 <= result_hour_24 < 12:
        result_hour_12 = result_hour_24
        result_period = 'AM'
    elif result_hour_24 == 12:
        result_hour_12 = 12
        result_period = 'PM'
    else:  # 13–23
        result_hour_12 = result_hour_24 - 12
        result_period = 'PM'

    # 7. Build the “(next day)” or “(n days later)” annotation
    if days_passed == 0:
        day_annotation = ''
    elif days_passed == 1:
        day_annotation = ' (next day)'              # Added leading space
    else:
        day_annotation = f' ({days_passed} days later)'  # Added leading space

    # 8. If a starting day was provided, compute the new day of week
    if starting_day:
        start_day_index = days.index(starting_day.lower())
        new_day_index = (start_day_index + days_passed) % 7
        new_day_name = days[new_day_index].capitalize()
        day_part = f', {new_day_name}'  # comma + space before the day name
    else:
        day_part = ''

    # 9. Format minutes with two digits (e.g. “03” instead of “3”)
    result_min_str = f'{result_min:02d}'

    # 10. Combine everything into the final return string
    new_time = (
        f'{result_hour_12}:{result_min_str} {result_period}'
        f'{day_part}'
        f'{day_annotation}'
    )

    return new_time