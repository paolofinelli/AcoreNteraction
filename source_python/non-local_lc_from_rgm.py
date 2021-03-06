import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colorss
import matplotlib.animation as animation
import shutil
import imp
from matplotlib import cm, colorbar
from matplotlib.ticker import FormatStrFormatter
from matplotlib.collections import LineCollection

import rad_interpolation

colors = [
    #      blue  orange  green   red      magenta
    '#1f77b4',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf'
]

datadir = "/home/kirscher/kette_repo/AcoreNteraction/data/"

MeVfm = 197.3161329

# a = ac * A^(1/3)
nlc = {
    'cm=1;B2=1;B3=4;ac=0.00245;ec=0.5439;ls=:':
    [[4, 0.900], [5, 0.900], [6, 1.000], [7, 1.100], [8, 1.300], [9, 1.400],
     [10, 1.600], [11, 1.800], [12, 1.900], [13, 2.000], [14,
                                                          2.200], [15, 2.300],
     [16, 2.400], [17, 2.500], [18, 2.600], [19, 2.700], [20,
                                                          2.800], [21, 2.900],
     [22, 3.000], [23, 3.100], [24, 3.200], [25, 3.200], [26,
                                                          3.300], [27, 3.400]],
    'cm=2;B2=1;B3=3;ac=0.00245;ec=0.5439;ls=-.':
    [[4, 0.900], [5, 0.900], [6, 1.000], [7, 1.100], [8, 1.300], [9, 1.400], [
        10, 1.600
    ], [11, 1.800], [12, 1.900], [13, 2.000], [14, 2.200], [15, 2.300], [
        16, 2.400
    ], [17, 2.500], [18, 2.600], [19, 2.700], [20, 2.800], [21, 2.900], [
        22, 3.000
    ], [23, 3.100], [24, 3.100], [25, 3.200], [26, 3.300], [27, 3.400], [
        28, 3.400
    ], [29, 3.500], [30, 3.500], [31, 3.600], [32, 3.700], [33, 3.700], [
        34, 3.800
    ], [35, 3.800], [36, 3.900], [37, 3.900], [38, 4.000], [39, 4.000], [
        40, 4.100
    ], [41, 4.200], [42, 4.200], [43, 4.300], [44, 4.300], [45, 4.400],
     [46, 4.400], [47, 4.500], [48, 4.500], [49, 4.600], [50, 4.600],
     [51, 4.600], [52, 4.700], [53, 4.700], [54, 4.800], [55, 4.800], [
         56, 4.900
     ], [57, 4.900], [58, 5.000], [59, 5.000], [60, 5.000], [61, 5.100]],
    'cm=3;B2=0;B3=4;ac=0.00245;ec=0.56;ls=:':
    [[4, 1.000], [5, 0.800], [6, 0.900], [7, 1.100], [8, 1.300], [9, 1.500], [
        10, 1.700
    ], [11, 1.900], [12, 2.000], [13, 2.200], [14, 2.400], [15, 2.500], [
        16, 2.600
    ], [17, 2.700], [18, 2.800], [19, 2.900], [20, 3.000], [21, 3.100], [
        22, 3.200
    ], [23, 3.200], [24, 3.300], [25, 3.400], [26, 3.400], [27, 3.500], [
        28, 3.500
    ], [29, 3.600], [30, 3.700], [31, 3.700], [32, 3.800], [33, 3.800], [
        34, 3.900
    ], [35, 4.000], [36, 4.000], [37, 4.100], [38, 4.200], [39, 4.200], [
        40, 4.300
    ], [41, 4.300], [42, 4.400], [43, 4.500], [44, 4.500], [45, 4.600], [
        46, 4.700
    ], [47, 4.700], [48, 4.800], [49, 4.900], [50, 4.900], [51, 5.000], [
        52, 5.100
    ], [53, 5.200], [54, 5.200], [55, 5.300], [56, 5.400], [57, 5.500], [
        58, 5.500
    ], [59, 5.600], [60, 5.700], [61, 5.800], [62, 5.800], [63, 5.900], [
        64, 6.000
    ], [65, 6.100], [66, 6.200], [67, 6.200], [68, 6.300], [69, 6.400], [
        70, 6.500
    ], [71, 6.600], [72, 6.700], [73, 6.800], [74, 6.800], [75, 6.900], [
        76, 7.000
    ], [77, 7.100], [78, 7.200], [79, 7.300], [80, 7.300], [81, 7.400],
     [82, 7.600], [83, 7.700], [84, 7.700], [85, 7.800], [86,
                                                          7.900], [87, 8.000],
     [88, 8.100], [89, 8.200], [90, 8.300], [91, 8.400], [92, 8.500], [
         93, 8.600
     ], [94, 8.600], [95, 8.800], [96, 8.900], [97, 9.000], [98, 9.100], [
         99, 9.200
     ], [100, 9.300], [101, 9.400], [102, 9.600], [103, 9.700], [104, 9.800]],
    'cm=4;B2=0;B3=4;ac=0.04;ec=0.56;ls=-':
    [[4, 0.900], [5, 0.900], [6, 0.900], [7, 1.600], [8, 2.000], [9, 2.400],
     [10, 2.800], [11, 3.300], [12, 3.700], [13, 4.100], [14, 4.600],
     [15, 5.000], [16, 5.500], [17, 6.000], [18, 6.500], [19, 6.900],
     [20, 7.300], [21, 8.000], [22, 8.500], [23, 9.000], [24, 9.600]]
}

data = [line for line in open(datadir + 'lc4_from_rgm_3-30.dat')][1:]
anz = len(data[0].strip().split()) - 1

f = plt.figure(figsize=(10, 8), dpi=95)
f.suptitle(r'$non-local$', fontsize=14)

ax1 = f.add_subplot(111)

ax1.set_xlabel(r'$A$', fontsize=12)
ax1.set_ylabel(r'$\lambda_c\;[fm^{-1}]$', fontsize=12)

ax1.plot(
    [float(line.strip().split()[0]) for line in data],
    np.array([float(line.strip().split()[1]) for line in data]),
    label=r'$(SVM) B(3)=4MeV$',
    c=colors[3],
    ls='-',
    lw=2)

intensities = np.random.rand(10)

cmaps = [
    plt.get_cmap('Blues'),
    plt.get_cmap('Greens'),
    plt.get_cmap('Greys'),
    plt.get_cmap('Reds')
]

idx = 0
for key in nlc.keys():

    ax1.plot(
        [aa[0] for aa in nlc[key]], [aa[1] for aa in nlc[key]],
        label=
        r'$B(2)=%4.1f\,MeV\;,\;\;B(3)=%4.1f\,MeV\;,\;\; a_{core}=%4.4f\cdot A^{%4.4f/3}$'
        % (float(key.split(';')[1].split('=')[1]),
           float(key.split(';')[2].split('=')[1]),
           float(key.split(';')[3].split('=')[1]),
           1. + float(key.split(';')[4].split('=')[1])),
        alpha=0.7,
        ls=str(key.split(';')[5].split('=')[1]),
        color=colors[int(key.split(';')[0].split('=')[1])])
    idx += 1

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width, box.height * 0.8])

plt.legend(
    loc='upper center',
    ncol=1,
    numpoints=1,
    fontsize=10,
    bbox_to_anchor=(0.5, 1.3))

#plt.show()
#exit()
strFile = 'non-local_lc_vgl.pdf'
if os.path.isfile(strFile):
    os.remove(strFile)
plt.savefig(strFile)
plt.savefig(strFile)