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
v_kb = 4
v_gb = 3

#Schieberegler
'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''
# Globale Variablen für Schiebregler:
# movingMode (Boolean): True, wenn der Schieber (Kreis) in Bewegung ist, False wenn nicht
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
movingMode = False
pointerPos = 0
pointerVal = 1.0

def setup(): #einmal
    size(1200, 600) #widht(x)/height(y)
    
def draw(): #immer

#Abrufen der globalen Variablen
    global length_podest
    global x1, y1, x2, y2, x3, y3, x4
    global running
    global konturfarbe_start, konturfarbe_reset
    global v_kb, v_gb

#Hintergrundfarbe
    background(224, 238, 224) #weil der alte Kreis immer gelöscht werden soll (wenn bei Setup, sieht man alle vorherigen Kreise)

#Titel
    textSize(30)
    fill(0)
    textAlign(CENTER) #Quelle Eugster Racipi
    text("Newton's first & second", width / 2, y3 + 40)

#Bemerkung/Beschreibung
    textSize(10)
    fill(0)
    textAlign(LEFT) #Quelle Eugster Racipi
    text("Diese Simulation stellt das erste und zweite Newtonsche Axiome dar. Sie visualisiert die Traegheit der Koerper und das Aktionsprinzip.", 10, height - 10)

#Laufbahn kleiner Kreis.
    noStroke() #keine Kontur Laufbahn
    fill(200) #Laufbahnfarbe
    rect(0, 170, length_podest, 60) #Podest
    rect(0, 230, 1200, 20) #Laufbahn
    triangle(length_podest, 170, length_podest + 150, 230, length_podest, 230) #Rampe
    
#kleiner Kreis
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0) #Konturfarbe
    fill(131, 139, 131) #Füllfarbe Kreis
    ellipse(x1, y1, 80, 80)
    
#Laufbahn grosser Kreis
    noStroke() #keine Kontur Laufbahn
    fill(200) #Laufbahnfarbe
    rect(0, 450, length_podest, 60) #Podest
    rect(0, 510, 1200, 20) #Laufbahn
    triangle(length_podest, 450, length_podest + 150, 510, length_podest, 510) #Rampe
    
#grosser Kreis
    strokeWeight(1) #Kontur Kreis, wie viele Pixel
    stroke(0) #Konturfarbe
    fill(131, 139, 131) #Füllfarbe Kreis
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
    
#Hindernis kleiner Ball
    fill(0)
    noStroke()
    rect(width - 50, 120, 2, 110)
    
#Hindernis gorsser Ball
    fill(0)
    noStroke()
    rect(width - 50, 350, 2, 160)

#Schieberegler
    draw_ruler(x3, y3 + 70, 130)
    
    v_kb = 4.0 + 4.0 * pointerVal * 0.01 #Min. Geschwindigkeit v_kb = 4, max. = + 100% von 4
    v_gb = 3.0 + 3.0 * pointerVal * 0.01 #Min. Geschwindigkeit v_kb = 4, max. = + 100% von 4
    
    #pro dirttel langsam, mittel, schwer
    if pointerVal <= 100 / 3:
        aktuell_v = "langsam"
    elif 100 / 3 <= pointerVal <= 100 * 2 / 3:
        aktuell_v = "mittel"
    else:
        aktuell_v = "schnell"
    
    textSize(10)
    textAlign(LEFT)
    fill(0)
    text(aktuell_v, x3, y3 + 90)

#Bewegungen / Quelle: Eugster Racipi
    if x3 <= mouseX <= x3 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung Start
        running = 1
        cursor(HAND)
    
    elif x4 <= mouseX <= x4 + 50 and y4 <= mouseY <= y4 + 50 and mouseButton == LEFT: #Bewegung reset
        running = 2   
        cursor(HAND)  

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
            y1 = y1 + 60.0 / 150.0 * v_kb #Berechnung delta y : delta x = 60 : 150 = ? : 5 -> ? = 2 
        if length_podest + 150 <= x1 < width - 90: #Bewegung auf dem Rest der Laufbahn
            x1 = x1 + v_kb
            
        #Bewegung grosser Ball
        if 0 <= x2 <= length_podest: #Bewegung auf Podest
            x2 = x2 + v_gb
        if length_podest < x2 < length_podest + 150: #Bewegung auf Rampe
            x2 = x2 + v_gb
            y2 = y2 + 60.0 / 150.0 * v_gb #Berechnung delta y : delta y = 60 : 150 = ? : 2 -> ? = 0.8
        if length_podest + 150 <= x2 < width - 120: #Bewegung auf dem Rest der Laufbahn
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
        
'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength): #Definition der Funktion -> Abhängig vom ObjX, etc.
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 12 #angepasst von 24 auf 12
    if pointerPos == 0: 
        pointerPos = objX #wenn Anfangsposition 0, soll der Regler bei objX beginnen (X Position)
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(3) #angepasst von 6 auf 3
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(100 / float(objLength) * (pointerPos - objX))
            
