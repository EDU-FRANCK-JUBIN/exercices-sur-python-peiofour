from turtle import *

color('red', 'blue')
begin_fill()

while True:
    forward(100)
    left(60)
    if abs(pos()) < 1:
        break
end_fill()
done()
