import time
import datetime
from time import sleep
from playsound import playsound 

file_path_sound = "/home/user/Загрузки/ajjfon_-_budilnik_radar_76666078.mp3"

def main():
    print("Input alarm-clock time in format YY-mm-dd-HH-MM-SS:")
    
    alarm_clock_time = input().split("-")

    alarm_clock_time_datetime = datetime.datetime(*map(int, alarm_clock_time))

    time_now = datetime.datetime.now()

    difference_time = alarm_clock_time_datetime - time_now

    sleep(difference_time.total_seconds)

    playsound(file_path_sound)

if __name__ == '__main__':
    main()