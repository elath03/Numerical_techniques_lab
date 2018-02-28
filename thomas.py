try:
   import numpy
   import matplotlib.pyplot as plt
except:
   import numpy

# Ai= 2*x, Bi= 2, Ci= 4*x
x_initial=input("Enter the initial value of x: ")
y_initial=input("Enter the initial value of y: ")
x_final=input("Enter the final value of x: ")
y_final=input("Enter the final value of y: ")
h=input("Enter h: ")
n=(x_final-x_initial)/h
print(n)
a=[]
b=[] 
c=[] 
d=[] 
y=[] 
c_final=[] 
d_final=[]
x=[]
i=1
x.append(x_initial)
while (i<n):
    x.append(x_initial+i*h)
    a.append((1/(h*h))-(2*(x_initial+i*h))/(2*h))
    b.append((-2/(h*h))+2)
    c.append((1/(h*h))+(2*(x_initial+i*h))/(2*h))
    i=i+1
d.append(4*(x_initial+h)-a[0]*y_initial)
x.append(x_final)
i=2
while (i<n-1):
    d.append(4*(x_initial+i*h))
    i=i+1
d.append(4*(x_final-h) - c[int(n-2)]*y_final)

c_final.append(c[0]/b[0])
i=1
while (i<n-1):
    c_final.append(c[i]/(b[i]-a[i]*c_final[i-1]))
    i=i+1

d_final.append(d[0]/b[0])
i=1
while (i<n-1):
    d_final.append((d[i]-a[i]*d_final[i-1])/(b[i]-a[i]*c_final[i-1]))
    i=i+1
y.append(y_final)
y.append(d_final[int(n-2)])
i=int(n-3)
count=1
while (i>=0):
    y.append(d_final[i]-c_final[i]*y[count])
    i=i-1
    count=count+1
y.append(y_initial)
y.reverse()
print(y)

plt.plot(x, y1, color='green', linestyle='None', marker='o',markerfacecolor='red', markersize=6)
plt.plot(x, y2, color='green', linestyle='None', marker='o',markerfacecolor='red', markersize=6)

plt.show()


