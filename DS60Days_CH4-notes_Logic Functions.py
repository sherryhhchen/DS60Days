# -*- coding: utf-8 -*-
"""
Part.2-1-04 NumPy 陣列邏輯函式 (Logic Functions)

目標:
1.陣列內容 (Array contents)
2.陣列型別偵測 (Array type testing)
3.比較 (Comparison)
4.邏輯操作 (Logical operations)
5.Truth 值測試 (Truth value testing)

@author: Sherry.HH.Chen
"""
# In[] Numpy 矩陣運算：element-wise operation
import numpy as np
A = np.array([[1,2],[3,4]],dtype='float64')
B = np.array([[5,0],[0,0]],dtype='float64')
A+B      # element-wise plus
C = np.array([[ 6.,  2.],
           [ 3.,  4.]])

# In[] Numpy 矩陣運算：matrix operation
import numpy as np

A = np.array([[1,2],[3,4]], dtype='float64')
B = np.array([[5,0],[0,0]], dtype='float64')
print('矩陣A：\n',A,
      '\n矩陣B：\n',B)
#e.g. 矩陣內積
np.dot(A, B)
print('矩陣內積(np.dot)：\n', np.dot(A, B))

#e.g. 矩陣轉置
print('矩陣轉置(.T)：\n', A.T)

#e.g. 反矩陣
A_rev = np.linalg.inv(A) #反矩陣
print('反矩陣：\n', A_rev)
print('矩陣 A 與 A 的反矩陣內積(為單位矩陣)：\n', np.dot(A, A_rev)) 

#e.g. 矩陣合併-垂直方向
V = np.vstack((A, B))
print('矩陣合併-垂直方向：\n',V)

#e.g. 矩陣合併-水平方向
H = np.hstack((A, B))
print('矩陣合併-水平方向：\n',H)

#e.g. 矩陣分割-垂直方向
VS = np.vsplit(V, 2) #切2份
print('矩陣分割-垂直方向：\n', VS)

#e.g. 矩陣分割-水平方向
HS = np.hsplit(H, 4) #切4份
print('矩陣分割-水平方向：\n', HS)

# In[] Numpy 陣列內容-.isnan() 

import numpy as np

n = np.array([1, 2, 0, np.nan, 3.])
print('np.isnan', np.isnan(n))

# In[] Numpy 陣列內容-.isfinite()：判斷是否為有限數
import numpy as np

print('np.isfinite(1)', np.isfinite(1))
print('np.isfinite(np.nan)', np.isfinite(np.nan))
print('np.isfinite(-np.nan)', np.isfinite(-np.nan))

# In[] Numpy 陣列內容-.isinf()、isposinf()、isneginf()：判斷元素是否為無限數

np.isinf([np.inf, -np.inf, 1.0, np.nan, np.PINF])
np.isposinf([np.inf, -np.inf, 1.0, np.nan, np.PINF])
np.isneginf([np.inf, -np.inf, 1.0, np.nan, np.PINF])

# In[] Numpy 陣列內容-.isnat()：判斷是否為日期時間

is_nat = np.isnat(np.array(['NaT', "2020-10-01", '2020-12-12 00:24:33'], dtype="datetime64[ns]"))

#非日期：回傳True；日期：回傳False
print('判斷是否為日期時間：\n',is_nat)

# In[] Numpy 陣列型別偵測-.isscalar()
"""
如果陣列元素為純量或是數字物件 (例如實數、複數、有理數) 、內建常數、字串的話，isscalar() 回傳 True 。需要留意的是 isscalar() 不是 element-wise 的，所以傳入值須為元素。
"""
a1 = np.array([1, 2, 3])
a1_scalar = np.isscalar(a1[2]) #要注意取的值是元素
print('陣列型別偵測-.isscalar()：\n', a1_scalar)

#傳入整個陣列，會回傳 False
a1_list = np.isscalar(a1)
print('回傳整個陣列：\n', a1_list)

#傳入內建常數：np.pi
pi_isscalar = np.isscalar(np.pi)
print('傳入內建常數，偵測isscalar：\n', pi_isscalar)

#傳入 0 維陣列，回傳 False
zero_ar = np.isscalar(np.array(3.0))
print('傳入 0 維陣列：\n', zero_ar)

# In[] Numpy 陣列型別偵測-判斷輸入的陣列元素為實數或是複數
import numpy as np
r = np.array([2, 3.0, 83])
rc = np.array([1+2j, 0+3j, 4.5, 20])

#判斷是否是實數、複數
r_isreal = np.isreal(r)
rc_isreal = np.isreal(rc)
print('陣列：\n', r,
      '\n判斷是否是實數.isreal()：\n', r_isreal)
print('陣列：\n', rc,
      '\n判斷是否是實數.isreal()：\n', rc_isreal)

rc_iscomplex = np.iscomplex(rc)
print('陣列：\n', rc,
      '\n判斷是否是複數.iscomplex()：\n', rc_iscomplex)

#判斷陣列中是否有實數、複數
rc_isrealobj= np.isrealobj(rc)
print('陣列：\n', rc,
      '\n判斷是否有實數.isrealobj()：\n', rc_isrealobj)

rc_iscomplexobj= np.iscomplexobj(rc)
print('陣列：\n', rc,
      '\n判斷是否有複數.iscomplexobj()：\n', rc_iscomplexobj)


# In[]  Numpy 廣播
import numpy as np
 
a = np.array([1,2,3])
b = 2
c = np.array([1,1,1])
c1 = 1
print(np.array_equal(c, c1), np.array_equiv(c, c1))


#元素相同形狀不同，但經廣播後，形狀相同
np.array_equal(np.array([1]), np.array([1,1,1,1]))
np.array_equiv(np.array([1]), np.array([1,1,1,1]))



# In[]  Numpy 陣列型別比較

# 形狀與元素值均相同
print('比較兩陣列形狀與元素是否相同：',
      np.equal(np.array([1, 2, 3]), np.array([1, 2, 3])))

#符合廣播規則的相等
print('符合廣播規則的相等`:',
      np.equal(np.array([1, 1, 1]), np.ones(1)))

# 不等於的比較，符合廣播規則
print('符合廣播規則的不等於比較：',
      np.not_equal([1, 2], [[1, 3],[1, 4]]))


# In[]  Numpy 陣列邏輯操作
import numpy as np

x = np.array([1,2,3,4])
y = np.array([1,2,26,5])
a = np.array([True, True, False, False])
b = np.array([True, False, True, False])

#AND：兩個都是True, 才是True
print('判斷 np.logical_and()：\n',
    np.logical_and(a, b),
    'a & b：')
print(a & b)

#OR：一個是True，就是True
print('判斷 np.logical_or()：\n',
    np.logical_or(a, b))

#NOT
print('判斷 np.logical_not()：\n',
    np.logical_not(b))

#XOR
print('判斷 np.logical_xor()：\n',
    np.logical_xor(a, b))

print('判斷 np.logical_xor()：\n',
    np.logical_xor(np.array([True, True, False, False]), np.array([True, False, True, False])))



# In[]  Numpy 陣列邏輯操作-判斷 XOR
"""
判斷兩個是否不一樣
不一樣 -> True
一樣 -> False
"""
print('np.logical_xor(True, True)：',
      np.logical_xor(True, True))

print('np.logical_xor(True, False)：',
      np.logical_xor(True, False))

print('np.logical_xor(False, True)：',
      np.logical_xor(False, True))

print('np.logical_xor(False, False)：',
      np.logical_xor(False, False))

print('np.logical_xor([True, True],[True, True])：',
      np.logical_xor([True, True],[True, True]))

print('np.logical_xor([False, False],[False, False])：',
      np.logical_xor([False, False],[False, False]))

print('np.logical_xor([True, False],[False, False])：',
      np.logical_xor([True, False],[False, False]))

print('np.logical_xor([True, True, False, False],[True, False, True, False])：',
      np.logical_xor([True, True, False, False],[True, False, True, False]))


# In[] Numpy 陣列邏輯操作-logical AND (廣播) 

"""
透過廣播產生符合條件的 2 個 True/False 陣列，並且進行 logical AND 操作。
"""

a = np.arange(5)
print(np.logical_and(a > 1, a < 4))


# In[]  np.all()：與

arr1 = np.array([0,1,2,3])
arr2 = np.array([True,True,True])

print(arr1.any())
#result:True
print(arr1.all())
#result:False
print(arr2.any())
#result:True
print(arr2.all())
#result:True




# In[]  np.any():或






