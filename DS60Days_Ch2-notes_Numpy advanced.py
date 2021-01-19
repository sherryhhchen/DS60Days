"""
D02-Numpy陣列重塑
"""

# In[] 載入 numpy
import numpy as np

# In[] Numpy陣列重塑:flatten()&ravel()
"""
(1).flatten() 和 .ravel() 可將多維陣列轉型為一維陣列，但兩者的差異在於回傳的是拷貝(copy)還是檢視(view)。
(2).flatten()回傳的是一份拷貝(copy)，所以對拷貝的修改不會影響原始矩陣；
(3).ravel()回傳的是一份檢視(view)，因此對檢視的修改，會直接影響到原始矩陣。

"""
#建立陣列
a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])

#使用flatten()重塑
f = a.flatten()
print('Array a.flatten():\n', f)  # -> [ 0  1  2  3  4  5  6  7  8  9 10 11]
print('Array a:\n', a)

#對f = a.flatten()進行修改
f[3] = 50
print('after f[3] = 50 ----- \n','f = \n', f)
print('after f[3] = 50 ----- \n','a = \n', a)

#------------------

#使用ravel()重塑
r = a.ravel()
print('Array r.ravel():\n', r)  # -> [ 0  1  2  3  4  5  6  7  8  9 10 11]
print('Array a:\n', a)

#對r = a.ravel()進行修改
r[3] = 100
print('after r[3] = 100 ----- \n','r = \n', r)
print('after r[3] = 100 ----- \n','a = \n', a)
# In[] Numpy陣列重塑：reshape() & resize()

#使用reshape()重塑
#將有12個元素形狀為(3,4)的a重塑為(2,6)
reshape_a1 = a.reshape(2,6)
print(reshape_a1)

reshape_a2 = np.reshape(a,(4,3))
print(reshape_a2)

reshape_a4 = a.reshape(6,-1)
print(reshape_a4)  #超過size會顯示 ValueError

#使用resize()重塑
# resize_a1 = a.resize(2, 6)
# print(resize_a1)

# resize_a2 = a.resize(4, 3)
# print(resize_a2)

# resize_a3 = a.resize(1, 4, refcheck=True)
# print(resize_a3)

# In[] 若 reshape 後的陣列元素值改變，會影響原陣列對應的元素值也跟著改變
a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])

reshape_a1 = a.reshape((2,6))
reshape_a1[1,3] = 555
print(reshape_a1)
print(a)
# In[]

a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])

reshape_a1 = a.reshape(2,3,2)


# In[] resize refcheck=True
print(b)
b = np.arange(15)
b.resize((2, 6), refcheck=True)
print(b)

# In[] np.newaxis()：增加軸數

a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])
print('a.shape：', a.shape)
b=a[:,np.newaxis,:].shape
print('a[:,np.newaxis,:].shape：', b)
b2=a[:,np.newaxis,:,np.newaxis,np.newaxis].shape
print('添加多個 np.newaxis：',b2)

# In[] NumPy 陣列的合併與分割-合併-concatenate()
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12],[13,14,15]])
z1=np.concatenate((x,y))

# In[] NumPy 陣列的合併與分割-合併-stack()
x0=np.array([[1,2,3],[4,5,6]])
y0=np.array([[7,8,9],[10,11,12]])
z0=np.stack((x0,y0),axis=0)
print('axis=0\n',z0)
print('shape: ',z0.shape)

x1=np.array([[1,2,3],[4,5,6]])
y1=np.array([[7,8,9],[10,11,12]])
z1=np.stack((x1,y1),axis=1)
print('axis=1\n',z1)
print('shape: ',z1.shape)

# In[] NumPy 陣列的合併與分割-合併-hstack()
xh=np.array([[1,2,3],[4,5,6]])
yh=np.array([[7,8,9],[10,11,12]])
print(xh)
print(yh)
zh=np.hstack((xh,yh))
print('hstack\n',zh)
print('xh.shape: ',xh.shape)
print('yh.shape: ',yh.shape)
print('zh.shape: ',zh.shape)

# In[] NumPy 陣列的合併與分割-合併-vstack()
xv=np.array([[1,2,3],[4,5,6]])
yv=np.array([[7,8,9],[10,11,12]])
zv=np.vstack((xv,yv))
print('vstack\n',zv)
print('xv.shape: ',xv.shape)
print('yv.shape: ',yv.shape)
print('zv.shape: ',zv.shape)


# In[] NumPy 陣列的合併與分割-分割-split()
import numpy as np

#建立一個有15個元素，形狀(5,3)的array
a = np.arange(15).reshape(5,3)
print(a)

#分成5等分
a5 = np.split(a, 5)
print(a5)

#indices_or_sections=[2,3]

a23 = np.split(a,[2,3])
print('indices_or_sections=[2,3]\n', a23)

# In[] NumPy 陣列的合併與分割-分割-hsplit()
import numpy as np

#建立一個有15個元素，形狀(5,3)的array
a = np.arange(30).reshape(5,6)
print(a)

#依水平軸切兩等分
ha = np.hsplit(a,2)
print('依水平軸切兩等分\n',ha)

#依水平軸切分，依照區段切
ha1 = np.hsplit(a, [2, 3, 6])
print('依水平軸切分，依照區段切\n', ha1)
# In[] NumPy 陣列的合併與分割-分割-vsplit()




# In[] 




# In[] 



# In[] 



# In[] 



# In[] 

# In[] 

# In[] 
