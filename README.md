Simple queue simulation
=======================

Source code for my blog post [] See the blog post for context.

This code is general for more than one machine per facility, but in the blog post, only the case involving one machine is discussed. In this implementation, only one single duration value is possible for all tasks.

The `base.py` file contains the classes that form the building blocks for the simulation. The code to generate the PNG files is also located here. This code relies on the [http://www.pythonware.com/products/pil/](Python Imaging Library).

The `statistics.py` file contains functions to compute mean and standard deviations of a list of values, and is essentially stolen from the standard module with the same name in Python 3.4 and newer.

The `simulate.py` file contains the code to produce the numbers used for the plots in the blog post. The numbers themselves are available in the `*.csv` files.

The `graphs.py` file contains the code to produce the set of PNG image files displayed in the post.

