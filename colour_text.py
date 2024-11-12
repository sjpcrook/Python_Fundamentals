from colorama import Fore, Back, Style


# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

import datetime

# today = datetime.datetime.now()
# birthday = datetime.datetime(2003, 7, 28)
# difference = today - birthday
# daystring = str(difference)
# pos = daystring.find(",")
# print(f"You have been alive for {daystring[:pos]}.")

today = datetime.datetime.now()
birthday = datetime.datetime(2003, 7, 28)
difference = today - birthday
print(f"You have been alive for {difference.days} days.")
