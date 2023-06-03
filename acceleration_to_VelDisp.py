import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('chichi.csv')

vel=np.cumsum(data.acc)
disp=np.cumsum(vel)

plt.subplot(3,1,1)
plt.plot(data.t,data.acc)
plt.subplot(3,1,2)
plt.plot(data.t,vel)
plt.subplot(3,1,3)
plt.plot(data.t,disp)
