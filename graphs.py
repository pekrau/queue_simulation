"""Discrete event simulation of queue of tasks for N number of machines.
Graphs for some instructive cases.
"""

from __future__ import unicode_literals, print_function, absolute_import

import base

N_MACHINES = 1
DURATION = 5.0

def write_case(n_tasks, utilization, ymax=400):
    simulation = base.Simulation(N_MACHINES, utilization)
    simulation.run(n_tasks, duration=DURATION)
    filename = "queue_{}_{}.png".format(N_MACHINES, int(100*utilization))
    simulation.write_image(filename, ymax=ymax)
    print('----', "{}%".format(int(100*utilization)), '----')
    print('tasks:', simulation.n_tasks)
    print('tasks delayed:', simulation.get_number_delayed())
    print('mean delay:', simulation.get_mean_delay())
    print('median delay:', simulation.get_median_delay())
    print('tmax:', simulation.tmax)


if __name__ == '__main__':
    write_case(12, 0.1, ymax=100)
    write_case(24, 0.2, ymax=175)
    write_case(70, 0.5, ymax=320)
    write_case(90, 0.7)
    write_case(100, 0.8)
    write_case(100, 0.9)
