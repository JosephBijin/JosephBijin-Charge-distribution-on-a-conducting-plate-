import numpy as np
import matplotlib.pyplot as plt
import random as rn
import time 



def Emt(x,y, Em, Ed):
    Etotal = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            Em[i,j] = (1*Q[i]*Q[j]/(np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)))
            Etotal = Etotal+Em[i,j]
        Ed[i] = (1*Q[i]/np.sqrt(d**2 + x[i]**2 + y[i]**2))
        Etotal = Etotal+ Ed[i]           
    return (Em, Ed, Etotal)
    

def Enew(Em,x,y, i, Q, d, Ed, Etotal):
    E = 0 
    Eold = 0
    for q in range(0,i):
            Eold = Eold+ Em[q,i]
            Em[q,i] = 1*Q[q]*Q[i]/(np.sqrt((x[q]-x[i])**2 + (y[q]-y[i])**2))
            E += Em[q,i]
    for j in range(i+1, len(x)):
            Eold =Eold+ Em[i,j]
            Em[i,j] = 1*Q[i]*Q[j]/(np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2))
            E = E+Em[i,j]
    Eold = Eold+ Ed[i]
    Ed[i] = (1*Q[i]/np.sqrt(d**2 + x[i]**2 + y[i]**2))
    E = E + Ed[i]     
    Etotal = Etotal - Eold + E
    return(Etotal, Em, Ed)

def plot(x,y,c,j):
 plt.clf()
 plt.figure()
 for i in range(len(x)):
  plt.scatter(x[i],y[i], c = c[i])
 plt.plot(0,0, 'o', color = 'red')
 plt.title(j)
 plt.xlim(-w,w)
 plt.ylim(-h,h)   
 plt.show()

def dis(x,y) :
   for i in range(len(x)):
        for j in range(i+1,len(x)):
            dist = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if dist <1:
                return (0 )
   return (1 )            
            
d = 25 
n=1000  #number of iteration 
qn = 100   #number of charges
x = np.zeros(qn) #x position 
y = np.zeros(qn) #y position 
h = 100 #height 
w = 100 #width
Q = np.zeros(qn)
c = []
Em = np.zeros([qn,qn])
Ed = np.zeros([qn])
delx =[-1,1] #step size
dely =[-1,1]
#initial position
for i in range(qn):
    x[i] = rn.randint(-h,h)
    y[i] = rn.randint(-w,w)
    if i < qn/2:        
        Q[i] = -1/qn
        c.append('b')
    else:
        Q[i] = -1/qn
        c.append('b')
j = 0        
plot(x,y,c,j)
Em, Ed, ET = Emt(x,y, Em, Ed)
print(ET)
L = []

for j in range(n):
 
  
  #plot(x,y,c,j)              
  for qr in range(0,qn):
     
     #qr = rn.randint(0,qn-1) #choosing charges randomly 
     xc = x[qr]
     yc = y[qr] 
     L.append(xc)
     L.append(yc)
     
     Et = ET
     Emt = Em
     Edt = Ed
     dx = rn.randint(-1,1)   #changing the postion randomly 
     dy = rn.randint(-1,1)     
     x[qr] = x[qr]+dx
     y[qr] = y[qr]+dy
     
     #checking if the position is within the box 
     if dis(x,y) == 0:
           x[qr] = xc
           y[qr] = yc
           j = j-1
           #print('x')
     elif (x[qr]>w or y[qr]>h) or (x[qr]<-w or y[qr]<-h):
           x[qr] = xc
           y[qr] = yc
           
           
     else:
           ET,Em, Ed = Enew(Em,x,y, qr, Q, d, Ed, ET)
           #checking if the energy condition is satisfied 
           if ET > Et:       
              x[qr] = xc
              y[qr] = yc
              ET = Et
              Em = Emt
              Ed = Edt
             
              
#plotting the result 

plot(x,y,c,j) 

distance = np.sqrt(x**2 + y**2)
D = distance
def density(distance,D, r1, r2):     
  
 keep =  (distance < r2) &  (distance  >= r1)
 D[keep] = r1 
 return (len(distance[keep]), D)

den = [] 
 
for r in np.arange(0,150):
    r1 = r
    r2 = (r1+1)
    a,b = density(distance,D,r1, r2)
    den.append(a)
    
plt.plot(np.arange(0,150), den)
print(den)   
plt.figure()
plt.hist(b)   
plt.hist(L) 

