add_time: Time Arithmetic Utility
A lightweight Python function for adding a duration (hours and minutes) to a 12-hour clock time (AM/PM), optionally tracking weekday changes. This utility returns a formatted string showing the resulting time, including the day of the week (if provided) and how many days later it is, if any.

Overview
add_time takes a starting time in 12-hour format (with AM/PM), a duration (hours:minutes), and an optional starting weekday. It computes the resulting clock time, adjusts for AM/PM transitions, calculates the number of days passed, and (if requested) determines the new weekday. The returned string follows these rules:

Times remain in “H:MM AM/PM” format.

If crossing midnight into the next calendar day, append (next day).

If more than 1 day passes, append (n days later).

If a weekday is supplied, append , Weekday right after the time, then the days-later annotation.

Features
12-hour to 24-hour conversion for intermediate arithmetic

Minute overflow handling (e.g., 11:55 AM + 0:10 → 12:05 PM)

Accurate day counting (handles durations spanning multiple days)

Optional weekday adjustment (case-insensitive input)

Pure Python, no external dependencies

How It Works
Parse the start time

Split into time_part (e.g. "11:43") and period (e.g. "PM").

Convert hours and minutes to integers.

Convert to 24-hour clock

If period is "PM" and hour ≠ 12, add 12.

If period is "AM" and hour = 12, set hour to 0.

Parse the duration

Split "H:MM" into hours and minutes.

Add minutes and handle overflow

total_minutes = start_minutes + duration_minutes

Any overflow beyond 60 yields extra hours via integer division.

Add hours (and any carried-over hours from minutes)

total_hours_24 = start_hour_24 + duration_hours + extra_hours

Compute days passed & final 24-hr hour

days_passed = total_hours_24 // 24

result_hour_24 = total_hours_24 % 24

Convert back to 12-hour format

0 → 12 AM, 1–11 → AM, 12 → 12 PM, 13–23 → (hour−12) PM.

Build the “(next day)” or “(n days later)” annotation

No annotation if days_passed == 0.

If 1, use (next day).

If >1, use (n days later).

Compute the new weekday (if provided)

Map weekdays to indices 0–6, add days_passed, then modulo 7.

Capitalize the resulting weekday and prepend with , .

Format minutes with leading zero

f"{minutes:02d}" ensures "07" instead of "7".

Concatenate into final string

"{hour}:{MM} {AM/PM}{, Weekday if given}{ (…days later) if needed}"

Installation
Copy the function into your project, or clone this repository.

Make sure you have Python 3.x installed.

No additional libraries are required—this uses only Python’s built-in str, int, and list operations.

Requirements
Python 3.6+

No external dependencies (standard library only)

License
This code is released under the MIT License. You are welcome to use, modify, and redistribute it, provided you include this notice in any distribution.

Feel free to open an issue or submit a pull request if you find a bug or have an enhancement suggestion!