x1 = 300
y1 = 200
x2 = 300
y2 = 400
x3 = 100
y3 = 275
stop = 300

def setup(): #once
    size(1200, 600) #widht(x)/height(y)
    
def draw(): #every time
    background(211, 211, 211)
    fill(255, 255, 255)
    
#kleiner Kreis
    global x1
    global y1
        
    x1 = x1
    ellipse(x1, y1, 100, 100)
    
    #triangle(150, 160, 190, 180, 150, 200)
    #rect(70, 170, 80, 20)
    line(200, 230, 1600, 230)
    triangle(0, 170, 200, 230, 0, 230)
    
#grosser Kreis
    global x2
    global y2
        
    x2 = x2
    ellipse(x2, y2, 200, 200)
        
    triangle(150, 360, 190, 380, 150, 400)
    rect(70, 370, 80, 20)
        
#force button 
    fill (139, 0, 0)
    ellipse(x3, y3, 50, 50)
    textSize(10)
    fill (0, 0, 0)
    text("click", 88, 271)
    text("here", 88, 283)
    
    if (mouseButton == LEFT): #Quelle processing.org: Interactivity
        x1 = x1 + 6
        x2 = x2 + 2
        
    global stop #(Quelle: Ammann & Sgier)
    if x1 > 1000:
        x1 = stop #zum stoppen?
        
    
    global stop #(Quelle: Ammann & Sgier)
    if x2 == 1000:
        x2 = stop #zum stoppen?
