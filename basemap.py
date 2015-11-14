from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

fig = plt.figure(1)
# create Basemap instance for Robinson projection.
m = Basemap(llcrnrlon=-20.,llcrnrlat=35.,urcrnrlon=60.,urcrnrlat=60.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            area_thresh=10000000.)
# draw costlines and coutries
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.5)
m.fillcontinents(color='0.8')

# convert lon and lat to map coordinates
x,y = m(0, 0)

# draw a point
point = plt.text(x,y,'Name', fontsize=20)

# this is called every frame
def init():
    #point.set_position([[],[]])
    return point,

start_lon = -20.
start_lat = 35.
end_lon = 60.
end_lat = 60.

# get slope
slope = (end_lat - start_lat) / (end_lon - start_lon)

# animation function.  This is called sequentially
def animate(i):
    x, y = m(i*0.1 + start_lon, (i*0.1) * slope + start_lat)
    point.set_position([x, y])
    return point,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               frames=100000, interval=1, blit=True)

plt.show()
