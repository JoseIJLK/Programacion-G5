from turtle import*
color('red','yellow')
begin_fill()
while True:
    forwant(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()