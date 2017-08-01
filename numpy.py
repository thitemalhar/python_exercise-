#Write a Python program to create a 3x3 matrix with values ranging from 2 to 10.

x = []
for i in range(2,11):
    x.append(i)

x = numpy.array(x)
#x = np.arange(2, 11).reshape(3,3)
print (x.reshape(3,3))
