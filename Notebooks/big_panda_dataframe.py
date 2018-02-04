
# coding: utf-8

# # Big Panda Dataframe

# Panda knows how to do lots of things with big data sets, so figure out how to create a panda dataframe.

# In[1]:


get_ipython().run_cell_magic('capture', '', '%matplotlib inline\nimport numpy as np\nimport sympy as sp\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# To get equations the look like, well, equations, use the following.\nfrom sympy.interactive import printing\nprinting.init_printing(use_latex=True)\nfrom IPython.display import display\n\n# Tools for manipulating quaternions.\nimport Q_tools as qt;')


# The function range is a generator.

# In[2]:


qha = qt.QHArray()

qDf = pd.DataFrame(qha.range(q_start=qt.QH([0, 0, 0, 0]), q_delta=qt.QH([1, 0.1, 0.2, 0.3]), n_steps=1000))
qDf.tail(3)


# Need to check if Panda wants array format for data
# 

# In[3]:


qha = qt.QHaArray()

qDf = pd.DataFrame(qha.range(q_start=qt.QHa([0, 0, 0, 0]), q_delta=qt.QHa([1, 0.1, 0.2, 0.3]), n_steps=1000))
qDf.tail(3)

