import numpy as np
import PIL.Image as image
import pylab
import scipy.misc
import matplotlib

pic = image.open("00001.png")
array = np.asarray(pic)
small = np.zeros(shape=(32,32,3))
final = np.zeros(shape=(64,64,3))

x = 0
y = 0

for i in xrange(0,64,2):
    for j in xrange (0,64,2):
        small[x][y][0] = array[i][j][0]/4 + array[i+1][j][0]/4 + array[i][j+1][0]/4 + array[i+1][j+1][0]/4
        small[x][y][1] = array[i][j][1]/4 + array[i+1][j][1]/4 + array[i][j+1][1]/4 + array[i+1][j+1][1]/4
        small[x][y][2] = array[i][j][2]/4 + array[i+1][j][2]/4 + array[i][j+1][2]/4 + array[i+1][j+1][2]/4
        y = y + 1
        if( y == 32 ):
            x = x + 1
            y = 0

for i in xrange(0,64,1):
    for j in xrange(0,64,1):
        final[i][j][0] = small[i/2][j/2][0]
        final[i][j][1] = small[i/2][j/2][1]
        final[i][j][2] = small[i/2][j/2][2]

scipy.misc.imsave('outfile.png', final)
