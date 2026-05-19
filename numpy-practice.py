import numpy as np

np_height=np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight=np.array([65.4, 68.7, 59.2, 68.7, 63.2])
bmi=np_weight/np_height**2
print(bmi)