from turtle import *
import colorsys
tracer(20)
bgcolor("black")
h = 0.5
for i in range(158):
    c = colorsys.hsv_to_rgb(h,1,1)
    color()
    h += 0.004
    rt(150)
    for j in range(85):
        fd(i)
        rt(150)
    rt(78)
done()