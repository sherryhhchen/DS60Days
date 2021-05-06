# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 2021

Part.2-1-05 NumPy 統計函式 Universal Functions (ufunc)
範例目標:
1.順序統計量 (Order Statistics)
2.平均數與變異數
3.相關性
4.直方圖 (Histogram)


範例重點:
1.統計函式也須注意針對計算的軸 (axis) 與維度 (dimension)
2.直方圖 (Histogram) 需要配合套件 matplotlib.pyplot 使用

@author: Sherry.HH.Chen
"""

# In[] 最大值和最小值
import numpy as np
import time
np.random.seed(int(time.time()))
a = np.random.randint(1, 10, 6).reshape(2,3)
b = np.random.randint(1, 5, 3)
print('a =\n', a,
      '\nb =\n', b)

print('取單一陣列中的元素最大值\n',
      'np.max(a) = ', np.max(a),
      '\n a.max()=', a.max(),
      '\nnp.max(a) = ', np.min(a),
      '\n a.max()=', a.min())

print('\n比較兩個陣列中的元素最大、最小值',
      '\nnp.maximum(a, b) = ' , np.maximum(a, b),
      '\n np.minimum(a, b)=', np.minimum(a, b)) #在進行比較時，若有需要會利用到廣播 (bradcasting)

# In[] 最大值和最小值 - 當遇到 nan 時
import numpy as np
import time
#np.random.seed(int(time.time()))
a = np.random.randint(1, 10, 6).reshape(2,3)
b = np.random.randint(1, 5, 3)
print('a =\n', a,
      '\nb =\n', b)

print('\n當 np.maximum()、np.minimum() 遇到 nan：',
      '\n np.maximum([np.nan, 3, np.nan],[3 , 2, np.nan])= ' , 
      np.maximum([np.nan, 3, np.nan],[3 , 2, np.nan]),
      '\n np.minimum([np.nan, 3, np.nan],[3 , 2, np.nan])= ' , 
      np.minimum([np.nan, 3, np.nan],[3 , 2, np.nan])) 
      #如果是 nan 和 非nan 比較，會傳回 "nan"
      
print('\n\n當 np.fmax()、np.fmin()遇到 nan：',
      '\n np.fmax(a, b)= \n', np.fmax(a, b),
      '\n np.fmin([np.nan, 3, np.nan],[3 , 2, np.nan])=\n', np.fmin([np.nan, 3, np.nan],[3 , 2, np.nan]))
      #如果是 nan 和 非nan 比較，會傳回 "非 nan"

# In[] 百分位數 - percentile(), nanpercentile()
import numpy as np

p = np.arange(1,11).astype('float32').reshape(2,5)
print(p)
per = np.percentile(p, [25, 50])
per_0 = np.percentile(p, [25, 50], axis=0)
per_1 = np.percentile(p, [25, 50], axis=1)
print('\n per = ',per,
      '\n per_0 = ', per_0, 
      '\n per_1 = ', per_1)


# In[] 百分位數 - percentile(), nanpercentile() - 包含 nan
p1 = np.array([ 1.,  2.,  3.,  4,  5,  6,  7.,  8.,  9., np.nan, 11., 12., 13.,
       14., 15., np.nan, 17., 18., 19.])

print('np.percentile()：', np.percentile(p1, [25, 75]),
      'np.nanpercentile()：',np.nanpercentile(p1, [25, 75]))
# In[] 分位數

q = np.array([23,  2,  1, 18,  9, 25, 14, 48, 43,  9, 31,  8,  4,  7, 22,  4,  5, 25, 44, 13]).reshape(5, 4)
print(np.quantile(q, 0.25))
print(np.nanquantile(q, 0.25)) 

q_nan = np.array([23,  2,  1, np.nan,  9, 25, 14, 48, 43,  9, 31,  8,  4,  7, 22,  4,  5, 25, 44, 13])
print(np.quantile(q_nan, 0.25))
print(np.nanquantile(q_nan, 0.25)) 

print(np.nanquantile(q, 0.25, axis=0, keepdims=True))

# In[] 計算平均值：np.mean()、np.nanmean()

a = np.array([23,  2,  1, np.nan,  9, 25, np.nan, 
              48, 43,  9, 31,  np.nan]).reshape(3, 4)

print('np.mean(a) = ', np.mean(a),
      '\n np.nanmean(a) = ', np.nanmean(a))

#使用np.isnan()判斷陣列中是否有nan，然後再選擇要用np.mean()還是np.nanmean()
if not np.isnan(np.sum(a)):
    print("陣列中無 nan，忽略 nan 後的平均值為：", np.mean(a))
else:
    print("陣列中有 nan，忽略 nan 後的平均值為：", np.nanmean(a))

# In[] 平均值：average()

a = np.arange(6).reshape((3,2))
a_avg = np.average(a, axis=1, weights=[0.25, 0.75])
print(a, a_avg)

# In[] median(), nanmedian()：中位數

#當有 nan 時
a = np.nanmedian(np.array([[36, 15, np.nan, 39, 17],
                       [np.nan,  9, 37, np.nan, 28],
                       [49, np.nan, 17,  8, 13]]), axis=1)

b = np.median(np.array([[36, 15, np.nan, 39, 17],
                       [np.nan,  9, 37, np.nan, 28],
                       [49, np.nan, 17,  8, 13]]), axis=1)

print('np.nanmedian()', a,
      'np.median()',b)


# In[] 相關係數：corrcoef()
import numpy as np

x = np.random.randint(1, 20, 10).reshape(2, 5)
print(np.corrcoef(x))

# In[] Histogram：直方圖

#下面的例子是隨機產生包含 100 個 0 - 9 數字的二維陣列，計算 histogram。
a = np.random.randint(0, 10, 100).reshape(10, 10)
hist, bin_edges = np.histogram(a, bins=9)
print('\n hist =', hist, 
      '\n bin_edges = ',bin_edges)


#比較 histogram() 的結果與實際元素值的 count，下面的範例使用 np.unique() 來得到所有出現過的值與其 count (出現的次數)。
unique, counts = np.unique(a, return_counts=True)
print('\n unique = ', unique, 
      '\n counts = ', counts)

#若使用資料視覺化進行比較並觀察其分佈，可以產出下面的圖表
import matplotlib.pyplot as plt

plt.hist(a.reshape(-1), bins=9)