"""Discrete event simulation of queue of tasks for N number of machines.
Simulate and output statistics.
"""

from __future__ import unicode_literals, print_function, absolute_import

import csv

import base
import statistics


N_MACHINES = 1
N_TASKS = 1000
DURATION = 5.0
STEP = 0.025
N = 20

fraction_delayed_writer = csv.writer(open('fraction_delayed.csv', 'w'))
mean_delays_writer = csv.writer(open('mean_delays.csv', 'w'))
median_delays_writer = csv.writer(open('median_delays.csv', 'w'))

utilization = 0.0
while True:
    utilization += STEP
    if utilization >= (1.0 - 0.1*STEP): break
    simulation = base.Simulation(n_machines=N_MACHINES, utilization=utilization)
    fraction_delayed = []
    mean_delays = []
    median_delays = []
    for n in xrange(N):
        simulation.run(n_tasks=N_TASKS, duration=DURATION)
        fraction_delayed.append(simulation.get_number_delayed()/float(N_TASKS))
        mean_delays.append(simulation.get_mean_delay())
        median_delays.append(simulation.get_median_delay())
    fraction_delayed_writer.writerow((utilization,
                                      statistics.mean(fraction_delayed),
                                      statistics.sstdev(fraction_delayed)))
    mean_delays_writer.writerow((utilization,
                                 statistics.mean(mean_delays),
                                 statistics.sstdev(mean_delays)))
    median_delays_writer.writerow((utilization,
                                   statistics.mean(median_delays),
                                   statistics.sstdev(median_delays)))
