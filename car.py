import turtle 
  
  

def moving_object(move): 
    
    move.penup()
    move.forward(500)             

if __name__ == "__main__" : 
            
    move = turtle.Turtle() 
    turtle.register_shape('yellow.gif') 
    move.shape('yellow.gif')
    move.speed(1)
    move.shape('yellow.gif')
    move.shapesize(1)
    move.setheading(0)
    move.setposition(0, 0)              
    move.goto(0, 0)  
             

    while True : 
          
        # clear turtle work 
        move.clear()   
          
        # call function to draw ball 
        moving_object(move)    
