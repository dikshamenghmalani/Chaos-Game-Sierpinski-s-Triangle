import turtle 
pen = turtle.Turtle()

def triangle_draw(length,side):
    if(side == -1):
        pen.color("black","#E5E4E2")
    elif(side == 0):
        pen.color("black","#837E7C")
    elif(side == 1):
        pen.color("black","#000000")
        
    pen.begin_fill()
    pen.setheading(180)
    for i in range(3):
        pen.right(120)
        pen.forward(length)
    pen.end_fill()

def sierpinski_triangle(n,length,side):
    
    if(n == 1):
        triangle_draw(length,side)
        
    else:
        sierpinski_triangle(n-1,length,-1)
        
        pen.right(120)
        pen.forward(length*2**(n-2))
        
        sierpinski_triangle(n-1,length,0)
        
        pen.left(120)
        pen.forward(length*2**(n-2))
        
        sierpinski_triangle(n-1,length,1)
        
        pen.forward(length*2**(n-2))
        
length = 7
n = 7
sierpinski_triangle(n,length,-1)

turtle.done()
try:
    turtle.bye()   
except turtle.Terminator:
    pass