import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz
from PIL import Image

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

# Simple mouse click function to store coordinates
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    # print 'x = %d, y = %d'%(
    #     ix, iy)

    # assign global variable to access outside of function
    global coords
    coords.append((ix, iy))

    # Disconnect after 2 clicks
    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return

im = Image.open('bird.jpg')
x = np.arange(-10,10)
y = x**2

fig = plt.figure(1)
ax = plt.imshow(im)


coords = []

# Call click func
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show(1)

a = coords[0][0].astype(int)





print ('Integral between '+ str(coords[0][0].astype(int)) +' & ' + str(coords[0][1].astype(int))+' & ' +str(coords[1][0].astype(int)) + ' & '+str(coords[1][1].astype(int)))

