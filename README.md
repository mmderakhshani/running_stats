# Running Statistics

This is a repository containing a python script to calculate batch-based running mean and running variance. 
There are lots of papers and works proposing new algorithms. But in my implementation, I have used this 
[paper](https://www.jstor.org/stable/2683386) for estimating running mean and running variance 
for a stream of data given by server and others.

Using eqautions proposed by the main paper (specifically Equation 1.5), we can solve a problem as presented bellow:

## Problem Definition:
Assume that you have a server releasing its logs at a predefined time (time step). And, at each time step it generates 
a batch of data (a sequence of data) as bellow:
```
timestep1 : x1,x2,x3,x4,x5
timestep2 : x6,x7,x8,x9,x10
timestep1 : x11,x12,x13,x14,x15
.
.
.
```
we are going to calculate the running mean and running variance already seen so far until a specific time step. 
Here is my code:

```{python}
import math
import numpy as np

l = 10 * np.random.randn(1000,10)
print("Real Mean:", np.mean(l))
print("Real Var:", np.std(l)**2)

N_1_to_m = len(l[0,:])
T_1_to_m = np.sum(l[0,:])
S_1_to_m = np.sum((l[0,:] - (1/(N_1_to_m)) * T_1_to_m)**2)


for i in range(1, l.shape[0]):
	N_m_to_n = len(l[i,:])
	T_m_to_n = np.sum(l[i,:])
	S_m_to_n = np.sum((l[i,:] - (1 / N_m_to_n) * T_m_to_n)**2)
	

	T_1_to_n = T_1_to_m + T_m_to_n
	S_1_to_n = S_1_to_m + S_m_to_n + \
			   (((N_1_to_m)/(N_m_to_n * (N_1_to_m + N_m_to_n))) * (((N_m_to_n)/(N_1_to_m))* T_1_to_m - T_m_to_n)**2)

	T_1_to_m = T_1_to_n
	S_1_to_m = S_1_to_n
	N_1_to_m = N_1_to_m + N_m_to_n


print("Estimated Mean:", T_1_to_m / N_1_to_m)
print("Estimated Var:", S_1_to_m / N_1_to_m)
```
and here is the result:
```
Real Mean: -0.0323245170767
Real Var: 100.089475801
Estimated Mean: -0.0323245170767
Estimated Var: 100.089475801
```
