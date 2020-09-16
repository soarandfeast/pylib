import sys
from datetime import datetime as dt

def time_diff(time_begin_str, time_end_str):
    time_str_format = "%Y/%m/%d %H:%M:%S"
    return dt.strptime(time_end_str, time_str_format) - dt.strptime(time_begin_str, time_str_format)

def main(argv):
    if len(argv) < 2:
        print("Usage: time_diff.py <time_begin (%Y/%m/%d %H:%M:%S)> <time_end (%Y/%m/%d %H:%M:%S)>")
        print("       E.g. python3 time_diff.py \"2020/09/16 11:44:02\" \"2020/09/16 11:44:04\"")
    else:
        print(time_diff(argv[0], argv[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
