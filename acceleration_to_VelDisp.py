import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('chichi.csv')
acc=data.acc_g #acceleration: g
a=acc*981 #acceleration: cm/s^2

#time step
dt=data.t[1]-data.t[0]
#velocity time history
v=np.cumsum(a)*dt #unit of velocity: cm/sec
#displacement time history
d=np.cumsum(v)*dt #unit of displacement: cm

#plotting
plt.figure(figsize=(8,8))
plt.subplot(311)
plt.plot(data.t,acc) #acceleration in g
plt.xlabel('t')
plt.ylabel('acc(g)')

#plotting velocity time history
plt.subplot(312)
plt.plot(data.t,v) #acceleration in g
plt.xlabel('t')
plt.ylabel('velocity(cm/s)')

#plotting displacement time history
plt.subplot(313)
plt.plot(data.t,d) #acceleration in g
plt.xlabel('t')
plt.ylabel('displacement(cm)')

plt.tight_layout()
