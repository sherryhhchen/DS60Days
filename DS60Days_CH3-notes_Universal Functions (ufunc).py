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




# In[] Numpy陣列的運算 - np.exp()：歐拉數 (Euler's number) 及指數函式



# In[]



# In[]



# In[]



# In[]


