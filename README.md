Simple queue simulation
=======================

Source code for my blog post [] See the blog post for context.

This code is general for more than one machine per facility, but in
the blog post, only the case involving one machine is discussed. In
this implementation, only one single duration value is possible for
all tasks.

The `base.py` file contains the classes that form the building blocks
for the simulation. The code to generate the PNG files is also located
here. This code relies on the
[Python Imaging Library](http://www.pythonware.com/products/pil/).

The `statistics.py` file contains functions to compute mean and
standard deviations of a list of values, and is essentially stolen
from the standard module with the same name in Python 3.4 and newer.

The `simulate.py` file contains the code to produce the numbers used
for the plots in the blog post. The numbers themselves are available
in the `*.csv` files.

The `graphs.py` file contains code to produce CSV files for plots of various
parameters as function of the utilization. No such plots are shown in
the blog post, but can be generated using
e.g. [Plotly](https://plot.ly/). A few CSV files are included as
a service here. They contain data in the following columns:

1. Utilization, in fractions.
2. The parameter given by the CSV file name. An average of 20 runs.
3. The (sample) standard deviation, using the data from 20 runs.

The PNG files are the same as in the blog post.
