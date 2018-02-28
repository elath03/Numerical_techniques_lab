try:
   import numpy
   import matplotlib.pyplot as plt
except:
   import numpy

ex= input()
flag=ex
# Ai= (-1)*2*x, Bi= -1*2, Ci= (-1)*4*x
ele_y = []
ele_x = []
while(ex>0):
    x_initial=input("Enter the initial value of x: ")
    x_final=input("Enter the final value of x: ")
    h=input("Enter h: ")
    alpha1=input()
    beta1=input()
    gamma1=input()
    alpha2=input()
    beta2=input()
    gamma2=input()
    n=(int(x_final-x_initial)/h)
    print(n)
    y=[] 
    x=[]
    x.append(x_initial)
    i=1
    while (i<n):
        x.append(x_initial+i*h)
        i=i+1
    x.append(x_final)
    a=[]
    b=[]
    c=[]
    d=[]
    c_final=[] 
    d_final=[]
    i=1;
    while (i<n):
        a.append((1/(h*h))-((-1)*2*(x_initial+i*h))/(2*h))
        b.append((-2/(h*h))+2*(-1))
        c.append((1/(h*h))+((-1)*2*(x_initial+i*h))/(2*h))
        i=i+1
    b[0]=(b[0]-((2*beta1)/h)/(alpha1-(3*beta1)/(2*h))*a[0])
    c[0]=(c[0]+((beta1)/(2*h))/(alpha1-(3*beta1)/(2*h))*a[0])
    d.append((-1)*4*(x_initial+h)-(a[0]*gamma1*2*h)/(alpha1*2*h-3*beta1))

    i=2
    while (i<n-1):
        d.append((-1)*4*(x_initial+i*h))
        i=i+1
    a[int(n-2)]=(a[int(n-2)]-((beta2)/(2*h))/(alpha2+(3*beta2)/(2*h))*c[int(n-2)])
    b[int(n-2)]=(b[int(n-2)]+((2*beta2)/h)/(alpha2+(3*beta2)/(2*h))*c[int(n-2)])
    d.append((-1)*4*(x_final-h)-(c[int(n-2)]*gamma2*2*h)/(alpha2*2*h+3*beta2))

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
    y_final=0;
    y_initial=0;
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
    y[0]=(gamma1-(y[1]*4-y[2])*beta1/(2*h))/(alpha1- (3*beta1)/(2*h))
    y[int(n)]=(gamma2+(y[int(n-1)]*4-y[int(n-2)])*beta2/(2*h))/(alpha2+ (3*beta2)/(2*h));
    print(y)
    ex=ex-1
    ele_y.append(y)
    ele_x.append(x)
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

ax.set_xlabel('X')
ax.set_ylabel('Y')

font1 = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 12,
        }

font2 = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 12,
        }
ax.text(.6, 3.5, "h=.05  o ",fontdict=font1)
ax.text(.6, 3.7, "h=.01  + ",fontdict=font2)

plt.plot(ele_x[0], ele_y[0], color='red', linestyle='None', marker='o', markersize=6)
plt.plot(ele_x[1], ele_y[1], color='blue', linestyle='None', marker='+', markersize=6)
plt.show()



