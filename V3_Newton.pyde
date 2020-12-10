#X-Koordinaten vom Podest/Länge des Podestes
length_podest = 150

#Position kleiner Ball
x1 = length_podest / 2
y1 = 130

#Position grosser Ball
x2 = length_podest / 2
y2 = 380

#Position Start button
x3 = 1020
y3 = 30

#Position Reset button
x4 = 1100
y4 = 30

#Kontrollvariable, ob Programm läuft / Input von Herrn Hefti
running = 0  #0 = Anfang, 1 = Programm läuft/Start, 2 = Programm reset

#Konturfarbe der Buttons "Start" und "Reset" / Quelle: Gruppe Eugster, Racipi / die Farben switchen zwischen gelb (255, 255, 0) und schwarz (0, 0, 0)
konturfarbe_start = 0 #R & G Wert des RGB-Wert Start Button
konturfarbe_reset = 0 #R & G Wert des RGB-Wert Start Button

#Geschwindigkeiten kb = kleiner Ball, gb = grosser Ball
v_kb = 5
v_gb = 3

def setup(): #einmal
    size(1200, 600) #widht(x)/height(y)
    
def draw(): #immer

#Abrufen der globalen Variablen
    global running
    global konturfarbe_start, konturfarbe_reset
    global length_podest
    global v_kb, v_gb    

#Hintergrundfarbe
    background(224, 238, 224) #weil der alte Kreis immer gelöscht werden soll (wenn bei Setup, sieht man alle vorherigen Kreise)

#Titel
    textSize(30)
    fill(0)
    textAlign(CENTER)
    text("Newton's first", width / 2, y3 + 40)

#Bemerkung/Beschreibung
    textSize(10)
    fill(0)
    textAlign(LEFT)
    text("Diese Simulation stellt das erste Newtonsche Axiom dar. Es visualisiert die Trägheit der Körper, die durch die selbe Karft angetrieben werden, sich jedoch unterschiedlich schnell bewegen.", 10, height - 10)


#Laufbahn kleiner Kreis
    noStroke() #keine Kontur Laufbahn
    fill(200) #Laufbahnfarbe
    rect(0, 170, length_podest, 60) #Podest
    rect(0, 230, 1200, 20) #Laufbahn
    triangle(length_podest, 170, length_podest + 150, 230, length_podest, 230) #Rampe
    
#kleiner Kreis
    global x1 #Variable holen
    global y1
    
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0) #Konturfarbe kleiner Kreis
    fill(131, 139, 131) #Füllfarbe kleiner Kreis
    ellipse(x1, y1, 80, 80)
    
#Laufbahn grosser Kreis
    noStroke() #keine Kontur Laufbahn
    fill(200) #Laufbahnfarbe
    rect(0, 450, length_podest, 60) #Podest
    rect(0, 510, 1200, 20) #Laufbahn
    triangle(length_podest, 450, length_podest + 150, 510, length_podest, 510) #Rampe
    
#grosser Kreis
    global x2
    global y2
        
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0) #Konturfarbe kleiner Kreis
    fill(131, 139, 131) #Füllfarbe kleiner Kreis
    ellipse(x2, y2, 140, 140)
        
#Start button
    strokeWeight(1) #Konturdicke in Pixel
    stroke(konturfarbe_start, konturfarbe_start, 0)
    fill (193, 205, 193)
    rect(x3, y3, 50, 50) #50 Breite
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

#Bewegungen / Quelle: Eugster Racipi
    if x3 <= mouseX <= x3 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung Start
        running = 1
    
    elif x4 <= mouseX <= x4 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung reset
        running = 2     

#Anfangsphase, beide Buttons schwarz    
    if running == 0: 
        konturfarbe_start = 0
        konturfarbe_reset = 0

#Start        
    if running == 1:
        #Bewegung kleiner Ball
        if 0 <= x1 <= length_podest: #Bewegung auf Podest
            x1 = x1 + v_kb
        if length_podest < x1 < length_podest + 150: #Bewegung auf Rampe
            x1 = x1 + v_kb
            #y1 = y1 + 60 / 150 * v_kb #Berechnung delta y : delta x = 60 : 150 = ? : 5 -> ? = 2 
            y1 = y1 + 2 #Berechnung delta y : delta x = 60 : 150 = ? : 5 -> ? = 2 
        if length_podest + 150 <= x1 <= width - 100: #Bewegung auf dem Rest der Laufbahn
            x1 = x1 + v_kb
            
        #Bewegung grosser Ball
        if 0 <= x2 <= length_podest: #Bewegung auf Podest
            x2 = x2 + v_gb
        if length_podest < x2 < length_podest + 150: #Bewegung auf Rampe
            x2 = x2 + v_gb
            #dy = 60 / 150 * v_gb
            #y2 = y2 + dy #Berechnung delta y : delta y = 60 : 150 = ? : 2 -> ? = 0.8
            y2 = y2 + 1.2 #Berechnung delta y : delta y = 60 : 150 = ? : 2 -> ? = 0.8
        if length_podest + 150 <= x2 <= width - 100: #Bewegung auf dem Rest der Laufbahn
            x2 = x2 + v_gb
        
        konturfarbe_start = 255 #Start button leuchtet (gelb)
        konturfarbe_reset = 0
            
#Reset
    if running == 2:
        #reset kleiner Kreis
        x1 = length_podest / 2 #geht zu Startposition
        y1 = 130
        
        #reset grosser Kreis
        x2 = length_podest / 2 #geht zu Startposition
        y2 = 380
        
        konturfarbe_start = 0 
        konturfarbe_reset = 255 #Reset button leuchtet (gelb)
