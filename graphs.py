"""Discrete event simulation of queue of tasks for N number of machines.
Graphs for some instructive cases.
"""

from __future__ import unicode_literals, print_function, absolute_import

import base

DURATION = 5.0

def write_case(n_tasks, utilization, ymax=400):
    simulation = base.Simulation(n_machines=1, utilization=utilization)
    simulation.run(n_tasks=n_tasks, duration=DURATION)
    filename = "queue_{}.png".format(int(100*utilization))
    simulation.write_image(filename, ymax=ymax)
    print('----', "{}%".format(int(100*utilization)), '----')
    print('tasks:', simulation.n_tasks)
    print('tasks delayed:', simulation.get_number_delayed())
    print('mean delay:', simulation.get_mean_delay())
    print('mean positive delay:', simulation.get_mean_positive_delay())
    print('median delay:', simulation.get_median_delay())
    print('tmax:', simulation.tmax)


if __name__ == '__main__':
    write_case(24, 0.2, ymax=160)
    write_case(70, 0.5, ymax=320)
    write_case(100, 0.9, ymax=440)
