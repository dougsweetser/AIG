
# coding: utf-8

# # Quaternion Series Quantum Mechanics Doodles

# This notebook is about initially playing around with quaternion series as a .

# In[4]:


get_ipython().run_cell_magic('capture', '', '%matplotlib inline\nimport numpy as np\nimport sympy as sp\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# To get equations the look like, well, equations, use the following.\nfrom sympy.interactive import printing\nprinting.init_printing(use_latex=True)\nfrom IPython.display import display\n\n# Tools for manipulating quaternions.\nimport Q_tools as qt;')


# Start with 4 simple states:

# In[6]:


A = qt.QHStates([qt.QH([4,0,0,0]), qt.QH([0,1,0,0])])
B = qt.QHStates([qt.QH([0,0,1,0]), qt.QH([0,0,0,2]), qt.QH([0,3,0,0])])
Op = qt.QHStates([qt.QH([3,0,0,0]), qt.QH([0,1,0,0]), qt.QH([0,0,2,0]), qt.QH([0,0,0,3]), qt.QH([2,0,0,0]), qt.QH([0,4,0,0])])
Op4i = qt.QHStates([qt.QH([0,4,0,0])])
print("A:\n", A)
print("B:\n", B)
print("Op:\n", Op)
print("Op4i:\n", Op4i)


# What I did with these 4 states was to calculate the combinations using good old paper and pencil. So I did:
# 
# <A|A>
# (A|A) - my notation for *not* taking the conjugate of the first A
# <B|B>
# (B|B)
# Op|B>=Op|B)
# <A|Op
# (A|Op
# <A|Op|B>
# (A|Op|B)
# 
# The doodling took one page of work. The work can then be checked in this notebook using variations of a command run like so:

# In[11]:


print(qt.QHStates().product(bra=A, ket=B))


# Good, spots errors.

# In[10]:


print(qt.QHStates().product(bra=A, ket=B, operator=Op))


# I was able to confirm this result was correct. In general though, this stuff is going to get insanely complicated quickly.

# ## Bonus Problem

# See if you can write out an operator that is Hermitian. I have a very specific guess in mind, but have yet to try it.
