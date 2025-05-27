from vpython import *
g1 = graph(xtitle="t",ytitle="x",width=500, height=250)
f1 = gcurve(color=color.blue, label="x1")
f2 = gcurve(color=color.red, label="x2")
k = 10
m = 0.15
b = 5

left = sphere(pos=vector(-.2,0,0),radius=0.01, color=color.red)
right = sphere(pos=vector(0.2,0,0),radius=0.01, color=color.red)
x1 = 0.03
x2 = 0
x1dot = 0
x2dot = 0
car1 = box(pos=vector(-.07+x1,0,0),size=vector(0.04,0.02,0.02), color=color.yellow)
car2 = box(pos=vector(0.07+x2,0,0),size=vector(0.04,0.02,0.02), color=color.cyan)
spring1=helix(pos=left.pos, axis=car1.pos-left.pos, radius=0.01, thickness=0.003)
spring2 = helix(pos=car1.pos, axis=car2.pos-car1.pos, radius=0.005,thickness=0.003)
spring3 = helix(pos=right.pos, axis=car2.pos-right.pos, radius = 0.01, thickness=0.003)

t = 0
dt = 0.01

w1 = sqrt(k/m)
w2 = sqrt((k+2*b)/m)
A1 = 0.03
A2 = 0.03


while t<5:
  rate(100)

  F1 = -k*x1-b*(x1-x2)
  F2 = -k*x2 - b*(x2-x1)
  x1ddot = F1/m
  x2ddot = F2/m
  
  x1dot = x1dot + x1ddot*dt
  x2dot = x2dot + x2ddot*dt
  x1 = x1 + x1dot*dt
  x2 = x2 + x2dot*dt
  car1.pos = vector(-0.07+x1,0,0)
  car2.pos = vector(0.07+x2,0,0)
  
  spring1.axis=car1.pos-left.pos
  spring2.pos=car1.pos
  spring2.axis=car2.pos-car1.pos
  spring3.axis = car2.pos - right.pos

  t = t + dt
  f1.plot(t,x1+.05)
  f2.plot(t,x2+0.2)
