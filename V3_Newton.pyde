#Position kleiner Ball
x1 = 50
y1 = 130
#Position grosser Ball
x2 = 50
y2 = 380
#Position click here button
x3 = 1020
y3 = 30
#Position reset button
x4 = 1100
y4 = 30

running = False  

def setup(): #once
    size(1200, 600) #widht(x)/height(y)
    
def draw(): #every time
    fill(255, 255, 255)
    background(224, 238, 224) #weil der alte Kreis immer gelöscht werden soll (wenn bei Setup, sieht man alle Kreise)
    
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
    rect(0, 450, 100, 60) #Podest
    rect(0, 510, 1200, 20) #Laufbahn
    triangle(100, 450, 250, 510, 100, 510) #Rampe
        
#click here button 
    fill (193, 205, 193)
    rect(x3, y3, 50, 50) #50 Durchmesser
    textSize(10)
    fill (0, 0, 0)
    text("click", x3 + 15, y3 + 20)
    text("here", x3 + 15, y3 + 40)
    
#reset button 
    fill (193, 205, 193)
    rect(x4, y4, 50, 50) #50 Durchmesser
    textSize(10)
    fill (0, 0, 0)
    text("Reset", x4 + 15, y4 + 30)

#Bewegung keliner Kreis
    if 1020 <= mouseX <= 1150 and 30 <= mouseY <= 80:
        running = True
    else:
        running = False
        
    if running == True:
        #if (mouseButton == LEFT and 1020 <= mouseX <= 1150 and 30 <= mouseY <= 80 ):
        if 50 <= x1 <= 100: #Bewegung auf Podest
            x1 = x1 + 5
        if 101 <= x1 <= 250: #Bewegung auf Rampe
            x1 = x1 + 5
            y1 = y1 + 2 #Berechnung delta y : delta y = 60 : 150 = ? : 5 -> ? = 2
        if 251 <= x1 <= 1100: 
            x1 = x1 + 5
            
    if (mouseButton == LEFT and 1100 <= mouseX <= 1150 and 30 <= mouseY <= 80 ):
        x1 = 50 #geht zu Startposition
        y1 = 130
        
#Bewegung grosser Kreis
    if (mouseButton == LEFT and 1020 <= mouseX <= 1150 and 30 <= mouseY <= 80 ):
        if 50 <= x2 <= 100: #Bewegung auf Podest
            x2 = x2 + 2
        if 101 <= x2 <= 250: #Bewegung auf Rampe
            x2 = x2 + 2
            y2 = y2 + 0.8 #Berechnung delta y : delta y = 60 : 150 = ? : 2 -> ? = 0.8
        if 251 <= x2 <= 1100: 
            x2 = x2 + 2
            
    if (mouseButton == LEFT and 1100 <= mouseX <= 1150 and 30 <= mouseY <= 80 ):
        x2 = 50 #geht zu Startposition
        y2 = 380
        
