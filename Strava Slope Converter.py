
import matplotlib
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt
from itertools import groupby

af = pd.read_csv("/content/routes.csv", header = None, encoding="utf-8")
inputy = af[0].tolist()

l2 = [key for key, _group in groupby(inputy)]
print(l2)
c = []
e = []
k = -1
for i in range(len(inputy)-1):
  if inputy[i] != inputy[i+1]:
    k = k+1
    c.append(inputy[i])
    e.append(k)
  else:
    k = k+1
    e = e
c.append(inputy[-1])
e.append(len(inputy))
print(c)
print(e)

x = np.array(e)
y = np.array(c)

x_smooth = np.linspace(x.min(), x.max(), 400)
y_smooth = make_interp_spline(x, y)(x_smooth)

plt.plot(x_smooth,y_smooth)
plt.scatter(x, y, marker='o')

plt.show()

r = list(range(0, xxx)) #Your recorded number of lines in csv.
spl = UnivariateSpline(x_smooth, y_smooth, k=5, s=0)
ylist = [round(num, 12) for num in (spl(r).tolist())]
print(ylist)

with open(r'/content/route_points.xlsx', 'w') as fp:
    for i in ylist:
        # write each item on a new line
        fp.write("%s\n" % i)

