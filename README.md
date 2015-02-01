Simple queue simulation
=======================

Source code for my blog post [Why queues are inevitable](https://kraulis.wordpress.com/2015/01/31/why-queues-are-inevitable/)
See the blog post for context.

A few notes about the terminology: "Machine" means a processing unit,
which can be a care team in hospital care, or a DNA sequencing machine
at the NGI. "Task" is in the health care a patient with a particular
disease to be treated, while it is a sample (or set of samples) at
NGI.

This code is general for more than one machine per facility, but in
the blog post only the case involving one machine is discussed. In
this implementation, only one single duration value is possible for
all tasks.

The `base.py` file contains the classes that form the building blocks
for the simulation. The procedure to generate PNG files is also located
here. It relies on the
[Python Imaging Library](http://www.pythonware.com/products/pil/).

The `statistics.py` file contains functions to compute mean and
standard deviations of a list of values, and is essentially stolen
from the standard module with the same name in Python 3.4 and newer.

The `graphs.py` file contains the code to produce the PNG files shown
in the blog post. Those files are also in this repo.

The `simulate.py` file contains code to produce average numbers for
various scenarios. Those were intended to be presented in plots in the
blog post, but were left out, in the end. They were not needed to make
the point. You can view them using e.g. [Plotly](https://plot.ly/).
They contain data in the following columns:

1. Utilization, in fractions.
2. The parameter given by the CSV file name. An average of 20 runs.
3. The (sample) standard deviation, using the data from 20 runs.
