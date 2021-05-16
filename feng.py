import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def u(t):
    return np.array(t >= 0, dtype=np.int)

def x(n):
    fun_x=u(n-1)-u(n-5)
    return fun_x

def h(n):
    fun_h=u(n-2)-u(n-8)+u(n-11)-u(n-17)
    return fun_h

n=np.arange(0,17,1)
nc=np.arange(0,33,1)

xn=x(n)
hn=h(n)

conv_xy=signal.convolve(xn,hn)

plt.subplot(311)
plt.stem(n,xn)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.subplot(312)
plt.stem(n,hn)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.subplot(313)
plt.stem(nc,conv_xy)
plt.xlabel('n')
plt.ylabel('y[n]=x[n]*h[n]')
plt.show()