# -*- coding: utf-8 -*-
"""
DS60Days_CH3-example_Universal Functions (ufunc)

@author: Sherry.HH.Chen
"""

# In[] Numpy陣列的四則運算 - 相加
import numpy as np

#純量相加
a = 1
b = 2
c = a + b 
print('a = ', a,
      '\nb = ', b,
      '\na + b =',c)

#陣列相加-使用符號
ar_a = np.arange(5)
ar_b = np.random.randint(0,50,5)
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a + ar_b = ', ar_a+ar_b)

#陣列相加-使用函式
print('np.add(ar_a,ar_b) = ',np.add(ar_a,ar_b))

"""
若是兩個陣列形狀不相同的話，遵循廣播規則，下面的例子可以正常運算。
"""

ar_a = np.arange(5)
ar_c = np.random.randint(0,50, size=(2,5))

print('ar_a =', ar_a,
      '\nar_c =', ar_c,
      '\nar_a + ar_c = ', ar_a+ar_c)

# In[] Numpy陣列的四則運算 - 相減
import numpy as np
#純量相減
a = 1
b = 2
c = a - b 
print('a = ', a,
      '\nb = ', b,
      '\na - b =',c)

#陣列相減-使用符號
ar_a = np.arange(5)
ar_b = np.random.randint(0,50,5)
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a - ar_b = ', ar_a-ar_b)

#陣列相減-使用函式
print('np.subtract(ar_a,ar_b) = ',np.subtract(ar_a,ar_b))

# In[] Numpy陣列的四則運算 - 相乘
#純量相乘
a = 1
b = 2
c = a * b 
print('a = ', a,
      '\nb = ', b,
      '\na * b =',c)

#陣列相乘-使用符號
ar_a = np.arange(5)
ar_b = np.random.randint(0,50,5)
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a * ar_b = ', ar_a*ar_b)

#陣列相乘-使用函式
print('np.multiply(ar_a,ar_b) = ',np.multiply(ar_a,ar_b))

# In[] Numpy陣列的四則運算 - 相除
#純量相除
a = 1
b = 2
c = a / b 
print('a = ', a,
      '\nb = ', b,
      '\na / b =',c)

#陣列相除-使用符號
ar_a = np.array([2,4,6,8,10])
ar_b = np.array([2,4,2,2,5])
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a / ar_b = ', ar_a/ar_b)

#陣列相除-使用函式
print('np.divide(ar_a,ar_b) = ',np.divide(ar_a,ar_b))

# In[] Numpy陣列的四則運算 - 求餘數

#純量求餘數
a = 11
b = 2
c = a % b 
print('a = ', a,
      '\nb = ', b,
      '\na % b =',c)
#陣列求餘數-使用符號
ar_a = np.array([3,17,7,8,10])
ar_b = np.array([2,4,2,3,5])
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a % ar_b = ', ar_a%ar_b)

#陣列求餘數-使用函式
print('np.mod(ar_a,ar_b) = ',np.mod(ar_a,ar_b))
# In[] Numpy陣列的運算 -.sum()：根據指定的軸計算陣列元素值加總

a = np.array([3,6,2,6,8])
print('a.sum() = ', a.sum())
print('np.sum(a) = ', np.sum(a))


# In[]Numpy陣列的運算 -.power()：次方

a = 2
b = 3
c = a ** b 
print('a = ', a,
      '\nb = ', b,
      '\na ** b =',c)
#陣列求次方-使用符號
ar_a = np.array([3,1,4,8,10])
ar_b = np.array([2,4,2,3,5])
print('ar_a =', ar_a,
      '\nar_b =', ar_b,
      '\nar_a ** ar_b = ', ar_a**ar_b)

#陣列求次方-使用函式
print('np.power(ar_a,ar_b) = ',np.power(ar_a,ar_b))

# In[] Numpy陣列的運算 - np.sqrt()：平方根

a = np.array([9,4,144,36,8])
print(np.sqrt(a))



# In[] Numpy陣列的運算 - np.exp()：歐拉數 (Euler's number) 及指數函式

e = np.e #歐拉常數
print(e)

np.exp(3)
print('np.exp(1) =', np.exp(3))
print('np.exp(np.arange(5)) =', np.exp(np.arange(5)))

# In[] Numpy陣列的運算 - 對數

import numpy as np
#以np.log10()為例
x = np.log10(np.array([1, 10, 100, 1000, 10000]))
print(x)


#若是log(負數)，則會產生nan常數
# import warnings 
# warnings.filterwarnings('ignore')

y = np.log([-1,2,1])
print(y)

# In[] Numpy陣列的運算 - 取近似值
"""
IEEE 754 的"四捨五取最近偶數六入"
"""
a = np.array([1.65, 1.55, 1.46, 1.45, 1.44, -3.57, 2.0])
print('a',a)
a_round = np.round(a, decimals=1)
print('a_round', a_round)

# Round至最近的整數
print('np.rint(a)',np.rint(a))

# 無條件捨去小數點
print('np.trunc(a)',np.trunc(a))

# 向下取整數
print('np.floor(a)', np.floor(a))

# 向上取整數
print('np.ceil(a)',np.ceil(a))
      
# 向0的方向取整數
print('np.fix(a)', np.fix(a))


# In[] Numpy陣列的運算 - 取絕對值：np.abs(), np.absolute(), np.fabs()

a = np.array([1.65,  1.55, -3.57,  2. ])
print('np.abs', np.abs(a))
print('np.absolute', np.absolute(a))
print('np.fabs', np.fabs(a))

#傳入複數至 fabs() 的話則會產生錯誤。
print('np.abs', np.abs(1+2j))
print('np.absolute', np.absolute(1+2j))
print('np.fabs', np.fabs(1+2j))








