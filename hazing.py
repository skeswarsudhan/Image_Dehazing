from skimage.transform import resize

n = 10
p = np2.empty(n, dtype=float)
# m = np2.empty(n, dtype=float)
for i in range(1, n + 1):
    img = '\\land_' + str(i)

    i1 = cv2.imread(r'C:\Users\S.K.ESWARSUDHAN\Desktop\sip\Land' + img + '.tif')
    i = cv2.imread(r'C:\Users\S.K.ESWARSUDHAN\Desktop\sip\smoke6.jpg')
    i3 = resize(i1, (800, 800))
    B = resize(i, (800, 800))

    i4 = np.zeros((800, 800, 3))

    for a in range(800):
     for b in range(800):
        i4[i, j, 0] = max(i3[i, j, 0], B[i, j, 0])
        i4[i, j, 1] = max(i3[i, j, 1], B[i, j, 1])
        i4[i, j, 2] = max(i3[i, j, 2], B[i, j, 2])

    import matplotlib.pyplot as plt
    plt.imshow(i4)
    plt.show()
    cv2.imwrite(r'C:\Users\S.K.ESWARSUDHAN\Desktop\sip\result_haze\result_' + str(i) + '.tif', HazeCorrectedImg)