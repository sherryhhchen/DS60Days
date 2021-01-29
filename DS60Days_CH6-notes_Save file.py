# -*- coding: utf-8 -*-
"""
範例目標:
運用 Numpy 讀取或輸出不同檔案格式

範例重點:
1.注意不同檔案格式有不同的讀取、輸出方式
2. .npy 與 .npz 格式是NumPy的檔案格式，透過 save()、savez()、load() 函式進行儲存與讀取
3.針對文字檔，可以使用 savetxt()、loadtxt()、genfromtxt() 來儲存與讀取

@author: Sherry.HH.Chen
"""
# In[] Numpy I/O - 單一陣列
import numpy as np 

#儲存單一陣列到 .npy 檔案，並用 numpy.load() 載入回傳陣列。
#with open 儲存內容
with open('one_array.npy', 'wb') as f:
    np.save(f, np.array([1,2]))

#載入並回傳檔案中的陣列
print(np.load('one_array.npy'))


# In[] Numpy I/O - 多陣列：使用np.save()

#呼叫 `numpy.save()` 時，儲存多個陣列時，內容會依序附加 (append) 在該檔案的最後。
with open('test.npy', 'wb') as f:
    np.save(f, np.array([1, 2]))
    np.save(f, np.array([1, 3]))
    np.save(f, np.array([2, 5]))
    np.save(f, np.array([1, 4]))

#載入的時候每一次 numpy.load() 就載入一個陣列。
with open('test.npy', 'rb') as f:
    a = np.load(f)
    b = np.load(f)
    c = np.load(f)
    d = np.load(f)

print(a, b, c, d)

# In[]  Numpy I/O - 多陣列：使用np.savez()
import numpy as np

x = np.arange(10)
y = np.array([1,2,3])
z = np.random.rand(10)
#print(x ,y, z)


#在儲存陣列時並指定陣列關鍵字 (array1, array2...)，若未指定的話預設會以 arr_0, arr_1... 關鍵字設定。

with open ('multi_array.npz', 'wb') as f:
    np.savez(f, array1=x, array2=y, array3=z)

#呼叫 numpy.load() 載入 .npz 檔案
npzfile = np.load('multi_array.npz')
#查看檔案類型
type(npzfile) #載入 .npz 檔案時，回傳的會是 NpzFile 類別


#透過file屬性，回傳list，可看到載入物件裡面包含3個陣列，名稱分別為 array1, array2, array3
print(npzfile.files)  #將陣列內容印出

# In[]  Numpy I/O - 多陣列：使用np.savez()
import numpy as np

x = np.arange(10)
y = np.array([1,2,3])
z = np.random.rand(10)
#print(x ,y, z)


#在儲存陣列時並指定陣列關鍵字 (array1, array2...)，若未指定的話預設會以 arr_0, arr_1... 關鍵字設定。

with open ('multi_array.npz', 'wb') as f:
    np.savez(f, x, y, z)

#呼叫 numpy.load() 載入 .npz 檔案
npzfile = np.load('multi_array.npz')
#查看檔案類型
type(npzfile) #載入 .npz 檔案時，回傳的會是 NpzFile 類別


#透過file屬性，回傳list，可看到載入物件裡面包含3個陣列，名稱分別為 array1, array2, array3
print(npzfile.files)  #將陣列內容印出


# In[] .savetxt()：將一維或二維陣列儲存到文字檔
import numpy as np

x = y = z = np.arange(0.0, 0.5, 1.0)

y = np.arange(10).reshape(2, 5)

#需注意，若儲存一維陣列，須加上中括號才能正常產生符號分隔檔格式，否則分隔符號會被忽略。

np.savetxt('test.out', [x], delimiter=',')

#使用 %load <filename> magic command 來查看檔案內容。
#%load test.out

#使用 fmt 引數可以指定輸出的格式，下例是指定科學記號的格式來輸出陣列值。
#在存檔時也可以加入 header / footer 做為檔案註解說明。
np.savetxt('test.out', x, fmt='%1.4e', delimiter=',', header='this is,\nheader', footer='this is footer')
#%load test.out

load_a = np.loadtxt('test.out', delimiter=',', dtype='f4')

print(load_a)


# In[]

from io import StringIO

data = u"  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(StringIO(data), delimiter=3))

# In[]



