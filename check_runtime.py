# -*- coding: utf-8 -*-
"""check_runtime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1al5LPQCWkOinP3xVhE3PazHHC6fqTcPa
"""

import time
a = [1,2,3,4]
start_time = time.time()

f1 = 1 + a[0]

print(f1)

end_time = time.time()
print(end_time-start_time)
# print(f3)

import time
start_time = time.time()
a = [1,2,3,4]
f2 = sum(a)
print(f2)
end_time = time.time()
print(end_time-start_time)