location = PVector(0, 200) 
velocity = PVector(1, 1)

def setup():
    size(400, 400)
    frameRate(45)
    rectMode(CENTER)
def draw():
    background(134)
    location.add(velocity)
    stroke(0)
    strokeWeight (10)
    fill(random(255), random(255), random(255)) # losowanie kolorów, to pójście na łątwiznę
    rect(location.x,location.y,120,120)
def mousePressed(): 
    loop() #nie zakańczasię, gdy kwadrat dochodzi do brzegu
