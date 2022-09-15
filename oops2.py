from ast import Pass


class Remote:
    Pass
class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1=Remote()
player1=Player()
if(remote1.isLeftPressed()):
    player1.moveLeft()
#  is leftPressed mein kya ho rha hn hme tension ni leni hn yh ek layer of abstraction hn
# abstaction means functionalitis se koi mtlb ni  bs featur  dekhte hn
# encapsulation means players ke saare method Player class mein bind hn
           