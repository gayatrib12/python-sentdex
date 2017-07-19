from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt
import time
 
#thresholding
 
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
 
    for eachRow in imageArray:
        for eachPix in eachRow:
            #print (eachPix)
            val1 = eachPix[:3]
            avgNum = reduce(lambda x, y: x + y, val1/len(val1))
            balanceAr.append(avgNum)
 
            #time.sleep(5)
 
    balance = reduce(lambda x, y: x + y, balanceAr/len(balanceAr))
 
    for eachRow in newAr:
        for eachix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]/len(eachPix[:3])) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 0
    return newAr
 
i = im.open('F:\SentDex\images\\numbers\\0.1.png')
iar = np.array(i)
 
i2 = im.open('F:\SentDex\images\\numbers\\y0.4.png')
iar2 = np.array(i2)
 
i3 = im.open('F:\SentDex\images\\numbers\\y0.5.png')
iar3 = np.array(i3)
 
i4 = im.open('F:\SentDex\images\\sentdex.png')
iar4 = np.array(i4)
 
threshold(iar2)
threshold(iar3)
threshold(iar4)
 
#print iar
 
 
fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0),rowspan = 4,colspan = 3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan = 4,colspan = 3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan = 4,colspan = 3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan = 4,colspan = 3)
 
ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
 
plt.show()
 