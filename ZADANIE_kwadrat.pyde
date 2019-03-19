location = PVector(0, 300) 
velocity = PVector(1, 1)

def setup():
    krotkaKolorow = ((255,0,0),(0,255,0),(0,0,255))
    size(600, 400)
    frameRate(60)
    rectMode(CENTER)
    stroke(*krotkaKolorow[2])
    fill(*krotkaKolorow[1])
def draw():
    background(134)
    location.add(velocity)
    rect(location.x,location.y,120,120)   
def mousePressed():
    loop()
