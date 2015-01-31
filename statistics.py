"Compute statistics."

from __future__ import unicode_literals, print_function, absolute_import

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/float(n) # the population variance
    return pvar**0.5

def sstdev(data):
    """Calculates the sample standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/float(n-1) # the sample variance
    return pvar**0.5

if __name__ == '__main__':
    import random
    data =  [random.random() for n in xrange(1000)]
    print(mean(data), pstdev(data), sstdev(data))
