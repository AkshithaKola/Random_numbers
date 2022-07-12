import numpy as np
import matplotlib.pyplot as plt
import scipy

x = np.linspace(-10,10,30)#points on the x axis
x1 = np.linspace(-10,10,30)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('T.dat',dtype='double')

for i in range(0,30):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

def T_Cdf(x):
    if x<0:
        return 1e-5
    elif (x>0 and x<1):
        return x**2/2
    elif (x>=1 and x<2):
        return 2*x - (x*x)/2 -1
    else:
        return 1

vec_cdf_t = scipy.vectorize(T_Cdf)

plt.plot(x[0:30].T,err,'o')#plotting the CDF
plt.plot(x1,vec_cdf_t(x1))
plt.grid() #creating the grid
plt.xlabel('$t$')
plt.ylabel('$F_T(t)$')
plt.legend(["Numerical", "Theory"])
plt.savefig('T_cdf.pdf')
plt.savefig('T_cdf.eps')
plt.show()