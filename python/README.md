# Usage

The module `multired.py` provides the class `multiplex_red`, which
implements the algorithm to reduce a multilayer network described in
the paper cited above.

In order to use it, you just need to 

    import multired as mr

in your python script and create a multiplex_red object. Please make
sure that "multired.py" is in PYTHONPATH. The constructor requires as
its first argument the path of a file which in turn contains a list of
files (one for each line) where the graph of each layer is to be
found.

The class provides one set of methods which perform the exact
evaluation of the Von Neumann entropy, and another set of methods
(those whose name end with the suffix `_approx`) which rely on a
polynomial approximation of the Von Neumann entropy. By default the
approximation is based on a 10th order polynomial fit of x log(x) in
[0,1], but the order of the polynomial can be set through the
parameter `fit_degree` of the constructor.

Several sample scripts can be found in the `test/` directory. You also
find a sample data set in the folder `sample_data/`. That is the
4-layer Noordin Top Terrorist multiplex network, originally provided
in:

> N. Roberts, S. F. Everton, Roberts and Everton "Terrorist Data:
> Noordin Top Terrorist Network" (Subset) (2011).

and extensively studied in:

> F. Battiston, V. Nicosia, V. Latora, "Structural measures for
> multiplex networks", Phys. Rev. E 89, 032804 (2014).

Please consider citing those papers if you use that data set in a
scientific work.


## Requirements

Python 2.x or 3.x with

    matplotlib==3.0.0
    numpy==1.15.2
    scipy==1.1.0
