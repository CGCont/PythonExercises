# own modules
# thirty party modules
# python modules

import datetime
#from datetime import timedelta
from datetime import timedelta, date
import myMath
from colorama import Fore, Style, init
init(convert = True)

print(
    datetime.date.today()
)

print(
    datetime.timedelta(minutes = 100)
)

print(
    timedelta(minutes = 150)
)

print(
    date.today()
)



print(myMath.add(78, 3))
print(myMath.susbtract(100, 25))
print(Fore.CYAN + "Hello World")

