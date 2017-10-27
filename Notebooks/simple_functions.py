
# coding: utf-8

# # Simple iPython Calculations

# This notebook contains examples of simple calculations so there is a record of "how to get things done".

# Start with common imports.

# In[11]:

get_ipython().magic('matplotlib inline')
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# To get equations the look like, well, equations, use the following two lines.
from sympy.interactive import printing
printing.init_printing(use_latex=True)


# Take the derivative of a function.

# In[4]:

[x, y] = sp.symbols(['x', 'y'])


# In[12]:

sp.diff(x * y * sp.sin(x), x)


# There are a few options on doing plots. **plot.ly** is a commercial product that has received good reviews. This is an older school way: create a function, a linear space of numbers, and plot it. 

# In[15]:

def f(x):
    """A polynomial."""
    return x**5 - 2 * x**4 + 3 * x**2 - 5 * x + 1

z = np.linspace(-2, 2)
plt.plot(z, f(z));


# In[ ]:



