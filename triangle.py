from turtle import *

color('red', 'yellow')
begin_fill()
pensize(10)
while True:
    forward(220)
    left(190)
    if abs(pos()) < 1:
        break
end_fill()
done()