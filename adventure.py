# A basic choose your own adventure game to review funcion defintions, loops, breaks ect.
#This is the space tutorial.

import random
import time
from textwrap import dedent


def displayIntro():
    print(dedent( """
        A putrid odor fills your nostrils. You are running through some sort of underground tunnel. You are completely devoid of memory.
        But, you are filled with a sense of urgency and you know you must run. Your feet pound against the gravel. Your head is pounding along with it.
        Do you remember how you got here? Do you even want to? n/ There is no time left now! Quick make a decision. East or West.
    """))

def choosePath():
    path = ""
    while path != "underground_west" and path != "underground_east":  #input validation if both equal to underground and surfae then its true
        path = input(" Which will you choose? (underground_west or underground_east): ")
        print()

    return path

def checkPath(chosenPath):
      print("You head  underground")
      time.sleep(5)
      print("It's cold.")
      time.sleep(8)
      print("So very cold")
      time.sleep(10)
      print("You wonder..")
      time.sleep(10)
      print("Where is everyone else?")
      print()

      correctPath = random.randint(underground_east, underground_west)

      if chosenPath == correctPath:
         print("You will get your answer soon enough.")
         print("That voice..")
         time.sleep(8)
         print("You don't recognize it. But it fills you with..")
         time.sleep(7)
         print("T")
         time.sleep(7)
         print("R")
         time.sleep(7)
         print("E")
         time.sleep(7)
         print("P")
         time.sleep(7)
         print("I")
         time.sleep(7)
         print("D")
         time.sleep(7)
         print("A")
         time.sleep(7)
         print("T")
         time.sleep(7)
         print("I")
         time.sleep(7)
         print("O")
         time.sleep(7)
         print("N")
      else:
         print(" You feel rush of electricity through your body.")
         print("Then nothing.")
        
        
              
            

displayIntro()
choosePath()
            
