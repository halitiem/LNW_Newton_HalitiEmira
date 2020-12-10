length_podest = 150

#Position kleiner Ball
x1 = length_podest / 2
y1 = 130
#Position grosser Ball
x2 = length_podest / 2
y2 = 380
#Position click here button
x3 = 1020
y3 = 30
#Position reset button
x4 = 1100
y4 = 30

#Kontrollvariable, ob Programm läuft
running = 0  

#Kontrollvariable, ob gedrückt
konturfarbe_start = 0
konturfarbe_reset = 0

def setup(): #once
    size(1200, 600) #widht(x)/height(y)
    
def draw(): #every time
    fill(255, 255, 255)
    background(224, 238, 224) #weil der alte Kreis immer gelöscht werden soll (wenn bei Setup, sieht man alle Kreise)
    textSize(30)
    fill(0)
    textAlign(CENTER)
    text("Newton's first", width / 2, y3 + 40)
    
    global running
    global konturfarbe_start, konturfarbe_reset
    global length_podest
    
#kleiner Kreis
    global x1 #Variable holen
    global y1
    
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0)
    fill(255, 0, 0)
    ellipse(x1, y1, 80, 80)
    
#Laufbahn kleiner Kreis
    noStroke()
    fill(200)
    rect(0, 170, length_podest, 60) #Podest
    rect(0, 230, 1200, 20) #Laufbahn
    triangle(length_podest, 170, length_podest + 150, 230, length_podest, 230) #Rampe
    
#grosser Kreis
    global x2
    global y2
        
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0)
    fill(0, 0, 255)
    ellipse(x2, y2, 140, 140)
    
#Laufbahn grosser Kreis
    noStroke()
    fill(200)
    rect(0, 450, length_podest, 60) #Podest
    rect(0, 510, 1200, 20) #Laufbahn
    triangle(length_podest, 450, length_podest + 150, 510, length_podest, 510) #Rampe
        
#Start button
    strokeWeight(1)
    stroke(konturfarbe_start, konturfarbe_start, 0)
    fill (193, 205, 193)
    rect(x3, y3, 50, 50) #50 Breit
    textSize(10)
    textAlign(CENTER) #Textposition
    fill (0, 0, 0)
    text("Start", x3 + 25, y3 + 30)
    
#Reset button 
    strokeWeight(1)
    stroke(konturfarbe_reset, konturfarbe_reset, 0)
    fill (193, 205, 193)
    rect(x4, y4, 50, 50) #50 Breit
    textSize(10)
    textAlign(CENTER) #Textposition
    fill (0, 0, 0)
    text("Reset", x4 + 25, y4 + 30)

#Bewegungen
    if x3 <= mouseX <= x3 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung Start
        running = 1
    
    elif x4 <= mouseX <= x4 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung reset
        running = 2     
    
    #Start        
    if running == 1:
        #Bewegung kleiner Kreis
        if 0 <= x1 <= length_podest: #Bewegung auf Podest
            x1 = x1 + 5
        if length_podest < x1 < length_podest + 150: #Bewegung auf Rampe
            x1 = x1 + 5
            y1 = y1 + 2 #Berechnung delta y : delta y = 60 : 150 = ? : 5 -> ? = 2
        if length_podest + 150 <= x1 <= width - 100: 
            x1 = x1 + 5
            
        #Bewegung grosser Kreis
        if 0 <= x2 <= length_podest: #Bewegung auf Podest
            x2 = x2 + 2
        if length_podest < x2 < length_podest + 150: #Bewegung auf Rampe
            x2 = x2 + 2
            y2 = y2 + 0.8 #Berechnung delta y : delta y = 60 : 150 = ? : 2 -> ? = 0.8
        if length_podest + 150 <= x2 <= width - 100: 
            x2 = x2 + 2
            
        konturfarbe_start = 255
        konturfarbe_reset = 0
            
            
    #reset
    if running == 2:
        #reset kleiner Kreis
        x1 = length_podest / 2 #geht zu Startposition
        y1 = 130
        
        #reset grosser Kreis
        x2 = length_podest / 2 #geht zu Startposition
        y2 = 380
        
        konturfarbe_start = 0
        konturfarbe_reset = 255
        
    if running == 0: 
        konturfarbe_start = 0
        konturfarbe_reset = 0
