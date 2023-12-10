from time import process_time_ns

def geom_rad_neefektivne(a0,r,N):
     for i in range(N):
         s=a0
         for j in range(i):
             s=s+a0*(r**(j+1))
         #print(s)

t1_start = process_time_ns() 
   
geom_rad_neefektivne(1,2,50000)
  
t1_stop = process_time_ns()
 
print("Trvanie behu funkcie arit v nanosekundach:\n", t1_stop-t1_start)  

print()
