import time
import psutil
from values import SYSTEM_TEST_RUNTIME


# The CPU usage results fetched with this are actually fairly accurate so leave as is !!!
def main():

    index = 0
    cpu_usage_percent_list = []

    print("Running a system diagnosis, please hold.")
    while index <= SYSTEM_TEST_RUNTIME:
        cpu_usage_percent_list.append(psutil.cpu_percent(interval=0.5))
        time.sleep(1)
        index = index + 1

    print("CPU usage per second below")
    print(cpu_usage_percent_list)


if __name__ == '__main__':
    main()