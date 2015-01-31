"""Discrete event simulation of queue of tasks for N number of machines.
Base classes and simple test.
"""

from __future__ import unicode_literals, print_function, absolute_import

import random
import heapq

# Python Imaging Library (PIL) http://www.pythonware.com/products/pil/
import Image, ImageDraw

SEED = 27182
random.seed(SEED)


class Machine(object):
    "Machine with capacity to handle one task. To be put into priority queue."

    def __init__(self):
        self.finished = 0.0

    def __cmp__(self, other):
        return cmp(self.finished, other.finished)


class Task(object):
    "One task to be performed. To be put into priority queue."

    def __init__(self, arrived, duration):
        self.t = arrived
        self.arrived = arrived
        self.duration = duration
        self.started = None

    def __cmp__(self, other):
        return cmp(self.t, other.t)

    def __str__(self):
        if self.started is None:
            return "Task {:.2f}".format(self.arrived)
        else:
            return str(self.started - self.arrived)

    def queue(self, machines):
        "Add this task to the queue; assign to machine, compute when finished."
        assert self.started is None
        machine = heapq.heappop(machines)
        # The machine is idle; start immediately
        if machine.finished < self.arrived:
            self.started = self.arrived
        # The machine is busy; start when it is done
        else:
            self.started = machine.finished
        self.t = machine.finished = self.started + self.duration
        heapq.heappush(machines, machine)        


class Simulation(object):
    "Perform and record simulation."

    def __init__(self, n_machines, utilization):
        self.n_machines = n_machines
        self.utilization = utilization

    def run(self, n_tasks, duration, verbose=False):
        self.n_tasks = n_tasks
        self.duration = float(duration)
        self.records = []
        self.delays = []
        machines = [Machine() for n in range(self.n_machines)]
        heapq.heapify(machines)
        # Create all tasks with arrival times independent of each other
        capacity = self.utilization * self.n_machines
        self.tmax = self.n_tasks * self.duration / capacity
        tasks = [Task(random.uniform(0.0, self.tmax), duration=self.duration)
                 for i in xrange(self.n_tasks)]
        heapq.heapify(tasks)
        while tasks:
            task = heapq.heappop(tasks)
            if task.started is None:
                task.queue(machines)
                heapq.heappush(tasks, task)
            else:
                finished = task.started + task.duration
                self.tmax = max(self.tmax, finished)
                self.records.append((task.arrived, task.started, finished))
                self.delays.append(task.started - task.arrived)
                if verbose:
                    print(task)
        self.delays.sort()

    def write_image(self, filename, ymax=400):
        YSTART = 20
        YOFFSET = 15
        YSTEP = 4
        img = Image.new('RGB', (int(self.tmax)+1, YSTART+ymax), 'gray')
        draw = ImageDraw.Draw(img)
        msg = "{} machines, {}% utilization".format(self.n_machines,
                                                    int(100*self.utilization))
        draw.text((4, 2), msg)
        y = YSTART + ymax - YOFFSET
        draw.text((4, y), 'time')
        tx, ty = draw.textsize('time')
        x = 4 + tx + 4
        y += ty / 2
        draw.line((x, y, x+30, y, x+30-10, y-5, x+30-10, y+5, x+30, y), 'white')
        y = YSTART
        for arrived, started, finished in self.records:
            y += YSTEP
            if y >= ymax:
                y = YSTART + YSTEP
            # High-light the delay in red
            if arrived != started:
                draw.rectangle((arrived, y, started, y+YSTEP), 'red')
            # Task processing is black
            draw.rectangle((started, y, finished, y+YSTEP), 'black')
            # Task arrival time in a separate lane, to show randomness
            draw.line((arrived, ymax-4, arrived, ymax+YSTEP-4), 'white')
        img.save(filename, 'PNG')

    def get_mean_delay(self):
        return sum(self.delays)/len(self.delays)
    
    def get_mean_positive_delay(self):
        positive_delays = [d for d in self.delays if d > 0.0]
        return sum(positive_delays)/len(positive_delays)
    
    def get_median_delay(self):
        return self.delays[len(self.delays)/2]

    def get_number_delayed(self):
        return len([d for d in self.delays if d > 0.0])


if __name__ == '__main__':
    N_MACHINES = 1
    N_TASKS = 100
    DURATION = 5.0
    UTILIZATION = 0.5
    simulation = Simulation(n_machines=N_MACHINES, utilization=UTILIZATION)
    simulation.run(n_tasks=N_TASKS, duration=DURATION)
    simulation.write_image("queue_{}_{}.png".format(N_MACHINES,
                                                    int(100*UTILIZATION)))
    print('tasks:', simulation.n_tasks)
    print('duration:', simulation.duration)
    print('tasks delayed:', simulation.get_number_delayed())
    print('mean delay:', simulation.get_mean_delay())
    print('median delay:', simulation.get_median_delay())
    print('tmax:', simulation.tmax)
