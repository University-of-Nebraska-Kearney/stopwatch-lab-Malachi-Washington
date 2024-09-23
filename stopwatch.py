# Import Library
import datetime

#identify constants
MINUTES_PER_HOUR=60
SECONDS_PER_MINUTE=60

# Get time for start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]

# Get time for stop
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]

#turn the time start and stop into total seconds
seconds_start=SECONDS_PER_MINUTE*(MINUTES_PER_HOUR*int(start_hour))+SECONDS_PER_MINUTE*int(start_minute)+float(start_second)
seconds_stop=SECONDS_PER_MINUTE*(MINUTES_PER_HOUR*int(stop_hour))+SECONDS_PER_MINUTE*int(stop_minute)+float(stop_second)

#calculate total seconds from start to stop
total_seconds= seconds_stop-seconds_start

#turn total seconds into total minutes
total_minutes= int(total_seconds//SECONDS_PER_MINUTE)

#turn total minutes into total hours
total_hours= int(total_minutes//MINUTES_PER_HOUR)

#calc. seconds remaining
seconds_remaining= float(total_seconds%SECONDS_PER_MINUTE)

#display time
print(f"{total_hours:02}:{total_minutes:02}:{seconds_remaining:.02f}")