
# coding: utf-8

# # Big Linear Set of Quaternions

# Generate a few quaternions using a class found in Q_tool_devo.

# In[1]:


get_ipython().run_cell_magic('capture', '', '%matplotlib inline\nimport numpy as np\nimport sympy as sp\nimport matplotlib.pyplot as plt\n\n# To get equations the look like, well, equations, use the following.\nfrom sympy.interactive import printing\nprinting.init_printing(use_latex=True)\nfrom IPython.display import display\n\n# Tools for manipulating quaternions.\nimport Q_tools as qt;')


# The class is call QHArray().

# In[2]:


qha = qt.QHArray()

for q_step in qha.range(q_start=qt.QH([0, 0, 0, 0]), q_delta=qt.QH([1, 0.1, 0.2, 0.3]), n_steps=10):
    print(q_step)


# Write out 10k to disk.

# In[3]:


with open('/tmp/10k.data', 'w') as datafile:
    for q_step in qha.range(q_start=qt.QH([0, 0, 0, 0]), q_delta=qt.QH([1, 0.1, 0.2, 0.3]), n_steps=10000):
        datafile.write("{}, {}, {}, {}\n".format(q_step.t, q_step.x, q_step.y, q_step.z))


# In[4]:


get_ipython().system(' wc -l /tmp/10k.data')
get_ipython().system(' tail -4 /tmp/10k.data')


# Bingo, bingo, we can make a large number of quaternions.
