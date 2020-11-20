import numpy as np
import matplotlib.pyplot as plt
x = [0,0,0,0,0,0]
y = [0,0,0,0,0,0]
actions_set = np.array([1,2,3,4,5,6])
for i in range(6):
    y[i]=np.log2(3 + 2 * actions_set[i])
    x[i]=(actions_set[i] /y[i])

plt.plot(np.arange(len(x)), x, label="")
plt.show()