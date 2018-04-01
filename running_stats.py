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