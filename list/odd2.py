import random
import time
from datetime import datetime


from os import getcwd
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

for i in range(5):

    rigth_this_minute = datetime.today().minute

    if rigth_this_minute in odds:
        print('This time seems a little odd.')
    else:
        print("Not an odd minute")

    sek = random.randint(1, 10)
    time.sleep(sek)
