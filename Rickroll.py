import time
from pygame import mixer

def Rcall():

        mixer.init()
        mixer.music.load('Rickroll.mp3')
        mixer.music.play()

        time.sleep(3)
        print('\033[1m' + '\nWELCOME TO RICKROLL' + '\033[0m')
        time.sleep(2)
        print('\033[1m' + '\nYES,YOU GET RICKROLLED' + '\033[0m')
        time.sleep(3)
        print('\033[1m' + '\nCONGRATULATION!' + '\033[0m')
        time.sleep(3)
        print('\033[1m' + '\nSO,WHAT NOW?' + '\033[0m')
        time.sleep(3)
        print('\033[1m' + '\nGRAB YOUR SEAT AND ENJOY' + '\033[0m')
        time.sleep(2.81)
        print('\033[1m' + '\nTHE MELODY OF RICKROLL' + '\033[0m')
        time.sleep(2)

        print("\n\nWe are not stanger to love")
        time.sleep(3.35)
        print("You know the rules and so do I")
        time.sleep(4.8)
        print("A full commitment's what I'm thinking of")
        time.sleep(4.2)
        print("You wouldn't get this from any other guy")
        time.sleep(4.08)
        print("I just wanna tell you how I'm feeling")
        time.sleep(4.63)
        print("Gotta make you understand")
        time.sleep(2.69)
        print("\nNever gonna give you up")
        time.sleep(2.5)
        print("Never gonna let you down")
        time.sleep(2.1)
        print("Never gonna run around and desert you")
        time.sleep(3.9)
        print("Never gonna make you cry")
        time.sleep(2)
        print("Never gonna say goodbye")
        time.sleep(2.5)
        print("Never gonna tell a lie and hurt you")
        time.sleep(5.1)

        mixer.music.stop()

        print('\033[1m' + '\nTHANK YOU FOR LISTENING' + '\033[0m')
        print('\033[1m' + 'GOOD BYE' + '\033[0m')


if __name__ == '__main__':
        Rcall()
