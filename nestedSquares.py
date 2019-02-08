import turtle

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.speed(25)
    tess.pensize(3)
    draw_sq(tess, 20, 5)
    
def draw_sq(t, sz, squares):
    for i in range(squares):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        sz += 20
        t.penup()
        t.left(45)
        t.forward(-15)
        t.right(45)
        t.pendown()
        
if __name__ == "__main__":
    main()
