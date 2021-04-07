import matplotlib.pyplot as plt
import numpy as np

# read the image by using matplotlib
Image_initial = plt.imread("Bike.jpg")

# access the shape by using numpy.shape
x, y = Image_initial.shape

# state the sobel kernel
Ix = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Iy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# create ndarrays in the form of orginal image
Image_x = np.zeros([x, y])
Image_y = np.zeros([x, y])
Image_new = np.zeros([x, y])

# convolution step
for i in range(0, x-2):
    for j in range(0, y-2):
        Image_x_value = (Ix[0, 0] * Image_initial[i, j]) + \
                  (Ix[0, 1] * Image_initial[i, j + 1]) + \
                  (Ix[0, 2] * Image_initial[i, j + 2]) + \
                  (Ix[1, 0] * Image_initial[i + 1, j]) + \
                  (Ix[1, 1] * Image_initial[i + 1, j + 1]) + \
                  (Ix[1, 2] * Image_initial[i + 1, j + 2]) + \
                  (Ix[2, 0] * Image_initial[i + 2, j]) + \
                  (Ix[2, 1] * Image_initial[i + 2, j + 1]) + \
                  (Ix[2, 2] * Image_initial[i + 2, j + 2])

        Image_y_value = (Iy[0, 0] * Image_initial[i, j]) + \
                  (Iy[0, 1] * Image_initial[i, j + 1]) + \
                  (Iy[0, 2] * Image_initial[i, j + 2]) + \
                  (Iy[1, 0] * Image_initial[i + 1, j]) + \
                  (Iy[1, 1] * Image_initial[i + 1, j + 1]) + \
                  (Iy[1, 2] * Image_initial[i + 1, j + 2]) + \
                  (Iy[2, 0] * Image_initial[i + 2, j]) + \
                  (Iy[2, 1] * Image_initial[i + 2, j + 1]) + \
                  (Iy[2, 2] * Image_initial[i + 2, j + 2])
        
        # calculate the magnitude
        I = np.sqrt(pow(Image_x_value, 2.0) + pow(Image_y_value, 2.0))
        Image_new[i, j] = I

# show the outcome by using matplotlib.imshow and show        
plt.imshow(Image_new, cmap='gray')
plt.show()
