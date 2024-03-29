from datetime import datetime


'''
pass in the time string in the format of: 
a = "2020-03-01 00:00:00.758604
b = "2020-02-28 23:59:59.944674
interval = <time in hours>
return true if the time difference is 
less than or equal to interval
'''

def inHr(time1, time2, interval):
    t1 = datetime.strptime(time1[0:19], "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time2[0:19], "%Y-%m-%d %H:%M:%S")
    duration = abs(t1 - t2)
    duration_sec = duration.total_seconds()
    hours = duration_sec / 3600 
    return hours <= interval

# assuming receiving two strings a and b
# in the format of 
# yyyy-mm-dd HH:MM:SS.ssssss or
# yyyy-mm-dd HH:MM:SS

def filterToNotSpam(a, b):
    return not inHr(a, b, 0.05)