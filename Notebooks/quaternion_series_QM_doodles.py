
# coding: utf-8

# # Quaternion Series Quantum Mechanics Doodles

# This notebook is about initially playing around with quaternion series as a .

# In[1]:


get_ipython().run_cell_magic('capture', '', '%matplotlib inline\nimport numpy as np\nimport sympy as sp\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# To get equations the look like, well, equations, use the following.\nfrom sympy.interactive import printing\nprinting.init_printing(use_latex=True)\nfrom IPython.display import display\n\n# Tools for manipulating quaternions.\nimport Q_tools as qt;')


# Start with 4 simple states:

# In[2]:


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

# In[3]:


print(qt.QHStates().product(bra=A, ket=B))


# Good, spots errors.

# In[4]:


print(qt.QHStates().product(bra=A, ket=B, operator=Op))


# I was able to confirm this result was correct. In general though, this stuff is going to get insanely complicated quickly.

# ## Bonus Problem

# See if you can write out an operator that is Hermitian. I have a very specific guess in mind, but have yet to try it.

# We already know that the Euclidean product of any quaternion series generates a quaternion series that only has real numbers like so:

# In[5]:


print("<A|A>:\n", qt.QHStates().Euclidean_product(bra=A, ket=A))
print("Sum of <A|A>: ", qt.QHStates().Euclidean_product(bra=A, ket=A).summation())


# What kind of operator might shift these values while still keeping it all "real"? My guess is a "Hermitian" series. This has to be square the size of the series squared. What is on the diagonal should not matter. The off the diagonal must have its conjugate in the right place on the other size. Test this guess with a few big quaternions:

# In[6]:


U = qt.QH([1, 2, 3, 4], qtype="U")
V = qt.QH([4, -1, 0, 2], qtype="V")
Vc = qt.QH([4, 1, 0, -2], qtype="Vc")
W = qt.QH([2, -3, -5, 1], qtype="W")
UVW = qt.QHStates([U, V, Vc, W])
print("<A|UVW|A>:\n", qt.QHStates().Euclidean_product(bra=A, ket=A, operator=UVW))
print("Sum <A|UVW|A>:\n", qt.QHStates().Euclidean_product(bra=A, ket=A, operator=UVW).summation())


# The answer is a "no". Try something simpler.

# In[7]:


VVc = qt.QHStates([qt.QH().q_0(), V, Vc, qt.QH().q_0()])
print("<A|VVc|A>:\n", qt.QHStates().Euclidean_product(bra=A, ket=A, operator=VVc))
print("Sum <A|VVc|A>:\n", qt.QHStates().Euclidean_product(bra=A, ket=A, operator=VVc).summation())


# That was a surprise, seeing the non-negative terms in the 3-vector part of the states. Confirm this happens for the quaternion series B.

# In[8]:


q0 = qt.QH().q_0()
q1 = qt.QH().q_1()
UVWc = qt.QHStates([q0, U, V, U.conj(), q0, W, V.conj(), W.conj(), q0])
print("<B|UVWc|B>:\n", qt.QHStates().Euclidean_product(bra=B, ket=B, operator=UVWc))
print("Sum <A|UVW|A>:\n", qt.QHStates().Euclidean_product(bra=B, ket=B, operator=UVWc).summation())


# Bingo, bingo! The "uneven" cancellations are kind of impressive. Can one put non-zero values along the diagonal?

# In[9]:


q3 = qt.QH([-3,0,0,0])
q2 = qt.QH([2,0,0,0])
UVWc = qt.QHStates([q3, U, V, U.conj(), q1, W, V.conj(), W.conj(), q2])
print("<B|UVWc|B>:\n", qt.QHStates().Euclidean_product(bra=B, ket=B, operator=UVWc))
print("Sum <A|UVW|A>:\n", qt.QHStates().Euclidean_product(bra=B, ket=B, operator=UVWc).summation())


# So one can put whatever real valued quaternions down the diagonal.
