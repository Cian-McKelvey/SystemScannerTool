import time
import psutil
from values import SYSTEM_TEST_RUNTIME, MAX_CPU_PERCENTAGE
from equations import *
from algorithms import *
from plotter import Plotter


# The CPU usage results fetched with this are actually fairly accurate so leave as is !!!
def main():

    index = 0
    cpu_usage_percent_list = []

    print("Running a system diagnosis, please hold.\n")

    while index <= SYSTEM_TEST_RUNTIME:
        # Used because the first value returned calling cpu_percent is 0 and is ignored
        if index > 0:
            cpu_usage_percent_list.append(psutil.cpu_percent())
            time.sleep(1)
            index = index + 1
        else:
            time.sleep(1)
            index = index + 1

    print("CPU usage per second below")
    print(cpu_usage_percent_list)

    # Quick check if cpu usage is over required amount
    if is_cpu_over_max_usage(cpu_usage_percent_list, MAX_CPU_PERCENTAGE) is True:
        print("Warning!!! CPU usage recorded at over", MAX_CPU_PERCENTAGE, "%")

    lowest_cpu = find_lowest_value(cpu_usage_percent_list)
    highest_cpu = find_highest_value(cpu_usage_percent_list)

    print("\n")

    print(f"You had a maximum CPU usage of {highest_cpu}% and the lowest was {lowest_cpu}%")
    print(f"This gives a range of {int(highest_cpu - lowest_cpu)}% (rounded to the nearest whole number))")

    # Plotting cpu usage to a graph using a created plotter object defined in plotter.py
    # Since its only used to plot the graph it isn't named, just created to call the plot_graph function
    Plotter(list_obj=cpu_usage_percent_list,
            xaxis_name="Seconds Passed",
            yaxis_name="CPU Usage (As Percentage)",
            title="CPU Usage Graph").plot_graph()


if __name__ == '__main__':
    main()
    