import math
from time import process_time_ns

def geoSuc(a0, r, N):           #12.
    suc = a0
    for i in range(N):
        #print(suc)
        a0 = a0*r
        suc = suc+a0
        


t1_start = process_time_ns() 
   
geoSuc(1,2,50000)
  
t1_stop = process_time_ns()
 
print("Trvanie behu funkcie arit v nanosekundach:\n", t1_stop-t1_start)  
  
print()


