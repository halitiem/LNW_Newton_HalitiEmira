#Anfangsposition
x1 = 50
y1 = 130
#
x2 = 300
y2 = 400
#Position Button
x3 = 1100
y3 = 30

x4 = 1100
y4 = 530

def setup(): #once
    size(1200, 600) #widht(x)/height(y)
    

def draw(): #every time
    fill(255, 255, 255)
    background(211, 211, 211) #weil der alte Kreis immer gelöscht werden soll (wenn bei Setup, sieht man alle Kreise)
    
#kleiner Kreis
    global x1 #Variable holen
    global y1
    
    #strokeWeight(2)
    ellipse(x1, y1, 80, 80)
    #noStroke()
    rect(0, 170, 100, 60) #Podest
    rect(0, 230, 1200, 20) #Laufbahn
    triangle(100, 170, 250, 230, 100, 230) #Rampe
    
#grosser Kreis
    global x2
    global y2
        
    ellipse(x2, y2, 140, 140)
        
    triangle(150, 360, 190, 380, 150, 400)
    rect(70, 370, 80, 20)
        
#click here button 
    fill (139, 0, 0)
    rect(x3, y3, 50, 50) #50 Durchmesser
    textSize(10)
    fill (0, 0, 0)
    text("click", x3 + 15, y3 + 20)
    text("here", x3 + 15, y3 + 40)
    
#Reset button 
    fill (139, 122, 0)
    rect(x4, y4, 50, 50) #50 Durchmesser
    textSize(10)
    fill (0, 0, 0)
    text("Reset", x4 + 15, y4 + 30)

    
    if (mouseButton == LEFT and 1100 <= mouseX <= 1150 and 30 <= mouseY <= 80 ):
        if 50 <= x1 <= 100: #Bewegung auf Podest
            x1 = x1 + 5
        if 101 <= x1 <= 250: #Bewegung auf Rampe
            x1 = x1 + 5
            y1 = y1 + 2 #Berechnung
        if 251 <= x1 <= 1100: 
            x1 = x1 + 5
            
    if (mouseButton == LEFT and 1100 <= mouseX <= 1150 and 530 <= mouseY <= 580 ):
        x1 = 50 #geht zu Startposition
        y1 = 130
        
