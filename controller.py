# import libraries
import time
import keyboard
import pyfirmata

# set up arduino board
board = pyfirmata.Arduino('COM17')

# setup servo on pin 2
precision=50
angle  = 90                     # initial angle
vitesse = 5                      # vitesse
servox = board.get_pin('d:2:s') # pin to communicate to the servo with
# set up a function that will tell the servo to move to a specific position when called

servox.write(angle) # move servo to specified angle

def move(tx,ty,angle):
    tx_ref,ty_ref=120,50 #milieu de la fenetre
    if tx<tx_ref-precision and angle>5:
        angle-=vitesse
        servox.write(angle)
    if tx>tx_ref+precision and angle<175:
        angle+=vitesse
        servox.write(angle)
    return angle
def move2(tx,ty):
    tx_ref,ty_ref=120,50 #milieu de la fenetre
    if tx<tx_ref-precision or tx>tx_ref+precision :
        angle=(tx - 0) * (135 - 45) // (240 - 0) +45 
        servox.write(angle)