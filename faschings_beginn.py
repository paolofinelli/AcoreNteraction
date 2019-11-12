import numpy as np
import matplotlib.pyplot as plt

aIS0002Ahoch2d3 = np.array([[12, 1.0], [13, 1.1], [14, 1.2000000000000002], [
    15, 1.3000000000000003
], [16, 1.4000000000000001], [17, 1.5000000000000002], [
    18, 1.7000000000000002
], [19, 1.8000000000000003], [20, 1.9000000000000001], [21, 2.0], [22, 2.1], [
    23, 2.3000000000000003
], [24, 2.4000000000000004], [25, 2.5000000000000004], [26, 2.6], [
    27, 2.8000000000000003
], [28, 2.9000000000000004], [29, 3.1], [30, 3.2], [31, 3.3000000000000003], [
    32, 3.5000000000000004
], [33, 3.6], [34, 3.8000000000000003], [35, 3.9000000000000004], [36, 4.1],
                            [37, 4.2], [38, 4.3999999999999995], [39, 4.5]])

aIS0001Ahoch3d3 = np.array([[12, 1.1], [13, 1.2000000000000002], [
    14, 1.3000000000000003
], [15, 1.4000000000000001], [16, 1.6], [17, 1.7000000000000002], [
    18, 1.8000000000000003
], [19, 2.0], [20, 2.1], [21, 2.3000000000000003], [22, 2.4000000000000004], [
    23, 2.6
], [24, 2.8000000000000003], [25, 2.9000000000000004], [26, 3.1], [
    27, 3.3000000000000003
], [28, 3.5000000000000004], [29, 3.6], [30, 3.8000000000000003], [31, 4.0], [
    32, 4.200000000000003
], [33, 4.400000000000003], [34, 4.600000000000003], [35, 4.800000000000003],
                            [36, 5.0000000000000036], [37, 5.200000000000003],
                            [38, 5.300000000000004], [39, 5.5000000000000036]])

aIS0001Ahoch2d3 = np.array(
    [[12, 0.8], [13, 0.9], [14, 0.9], [15, 1.0], [16, 1.1],
     [17, 1.2000000000000002], [18,
                                1.3000000000000003], [19, 1.3000000000000003],
     [20, 1.4000000000000001], [21, 1.5000000000000002], [22, 1.6], [
         23, 1.7000000000000002
     ], [24, 1.8000000000000003], [25, 1.9000000000000001], [26, 2.0], [
         27, 2.1
     ], [28, 2.2], [29, 2.3000000000000003], [30, 2.4000000000000004], [
         31, 2.5000000000000004
     ], [32, 2.6], [33, 2.7], [34,
                               2.8000000000000003], [35, 2.9000000000000004],
     [36, 3.0000000000000004], [37, 3.1], [38, 3.2], [39, 3.3000000000000003]])

aIS0008Ahoch2d3 = np.array(
    [[2, 0.1], [3, 0.2], [4, 0.30000000000000004], [5, 0.5], [6, 0.6], [
        7, 0.7000000000000001
    ], [8, 0.9], [9, 1.0], [10, 1.2000000000000002], [11, 1.4000000000000001],
     [12, 1.6], [13, 1.7000000000000002], [14, 1.9000000000000001], [15, 2.1],
     [16, 2.3000000000000003], [17, 2.5000000000000004], [
         18, 2.7000000000000006
     ], [19, 3.000000000000001], [20, 3.200000000000001], [
         21, 3.4000000000000012
     ], [22, 3.6000000000000014], [23, 3.8000000000000016], [
         24, 4.000000000000002
     ], [25, 4.200000000000002], [26, 4.400000000000002], [
         27, 4.600000000000002
     ], [28, 4.8000000000000025], [29, 5.000000000000003], [
         30, 5.200000000000003
     ], [31, 5.400000000000003], [32, 5.5000000000000036], [
         33, 5.700000000000003
     ], [34, 5.800000000000003], [35, 6.0000000000000036], [
         36, 6.100000000000003
     ], [37, 6.200000000000004], [38,
                                  6.300000000000004], [39, 6.400000000000004]])

svmdata = np.array([[2, 0.38], [3, 0.5], [4, 0.67], [5, 0.85], [6, 1.05]])

f = plt.figure(figsize=(10, 4))
ax1 = f.add_subplot(111)
ax1.set_xlabel(r'$A$', fontsize=12)
ax1.set_ylabel(r'$\lambda_c [fm^{-1}]$', fontsize=12)
ax1.plot(svmdata[:, 0], svmdata[:, 1], 'ro', label=r'SVM data')
ax1.plot(
    aIS0001Ahoch2d3[:, 0],
    aIS0001Ahoch2d3[:, 1],
    label=r'$a=0.001\cdot A^{2/3}$')
ax1.plot(
    aIS0002Ahoch2d3[:, 0],
    aIS0002Ahoch2d3[:, 1],
    label=r'$a=0.002\cdot A^{2/3}$')
ax1.plot(
    aIS0001Ahoch3d3[:, 0], aIS0001Ahoch3d3[:, 1], label=r'$a=0.001\cdot A$')
ax1.plot(
    aIS0008Ahoch2d3[:, 0],
    aIS0008Ahoch2d3[:, 1],
    label=r'$a=0.008\cdot A^{2/3}$')
ax1.legend(loc=0, fontsize=14)
plt.show()