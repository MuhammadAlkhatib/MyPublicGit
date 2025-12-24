import numpy as np

r=np.random.RandomState(12)

# a1=r.choice(10,size=10,replace=False)
# print(a1)
# print(a1[3])
# print(a1[1])
# print(a1[-2])
# print(a1[:])
# print(a1[::])
# print(a1[:a1.size ])

# print(a1[:4])
# print(a1[2:5])
# print(a1[2:-1])
# print(a1[::-1])
# print(a1[2:8:2])
# print(a1[:-3])
# ======================================================
# a2=r.choice(50,size=(3,4),replace=False)
# print(a2)
# print(a2[1,2])
# print(a2[-2,3])
# print(a2[-1,-2])
# print(a2[2])
# print(a2[2,:2])
# print(a2[:2,:2])
# print(a2[:-1,:])
# print(a2[1:,1:3])

# ======================================================
# a3=r.choice(100,size=(3,3,4),replace=False)
# print(a3)
# print(a3[-1,-1,-1])
# print(a3[2,2,3])
# print(a3[1,1,2])
# print(a3[-2,-2,-2])
# print(a3[1])
# print(a3[1,:,:])
# print(a3[1,1:,2:])
# print(a3[:,1:,0:2])

# ======================================================
# arr1=np.array([[1,2,3,4],[4,5,6,7]])
# arr2=arr1
# print(arr1)
# print('----------')
# print(arr2)

# arr2[1,1]=30
# # print(arr1)
# # print('----------')
# # print(arr2)

# arr3=arr1.copy()
# arr3[0,0]=100
# print(arr1)
# print('----------')
# print(arr3)

# ========================================================
# a=np.array([[1,2,3,4],[5,6,7,8]])
# print(a)
# print(a.ndim)
# print(a.size)
# print(a.nbytes)
# print(a.itemsize)
# print(a.shape)
# print(a.reshape(4,2))
# print(a.reshape(4,-1))