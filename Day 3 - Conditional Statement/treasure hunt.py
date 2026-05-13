print(r'''
                _.--.
            _.-'_:-'||
        _.-'_.-::::'||
    _.-:'_.-::::::'  ||
    .'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
\..  ||:::::.-!()oo @!()@.-'_.|
'.'-;|:.-'.&$@.& ()$%-'o.'\U||
    `>'-.!@%()@'@_%-'_.-o _.|'||
    ||-._'-.@.-'_.-' _.-o  |'||
    ||=[ '-._.-\U/.-'    o |'||
    || '-.]=|| |'|      o  |'||
    ||      || |'|        _| ';
    ||      || |'|    _.-'_.-'
    |'-._   || |'|_.-'_.-'
    '-._'-.|| |' `_.-'
        '-.||_/.-'
\n\n\n''')

coin = r'''
               ,,==="""""""===,,
           ,==""' |\ |   /\   `""==,
        ,="'|\    | \|  /__\   /\  `"=,
      /"    |,"\  |  | /'  `\ /  )     "\
    /"  ,"  |                 `\/    /|  "\
   /'  |   ,                       /",|   `\
  /'   ",/"                           |    `\
 /'      I=I=I               ,d8ba,___      `\
/'     I=8=8=8=I_I_          88888P"""       `\
|   xXXXXXXXXXXXXXXXxIxx    ,888"             |
| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
`\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
 `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
  `\    /"\         1 9 9 4        \ /\    /'
   `\  "\,/'                   |\   `\ `  /'
     "\      /""\   |    |     |,'\     /"
       `"=,_ \__/   |__  |__   |    ,="'  
          `""=,__             __,=""'
               ``""=========""''
'''

crossroad = r'''
      🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴
   🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿
🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿

==================================================
                ← LEFT          RIGHT →
==================================================
🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴🌿🌴
   🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿
      🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴
'''

island = r'''
        .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
      ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~    *   *   *    ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~   /|\ /|\ /|\  ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~   /|\ /|\ /|\  ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~  _|||_|||_|||_  ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~ /~~~~~~~~~~~~~~~\ ~  ~  ~  ~  ~  ~  ~  ~
~  ~  ~  ~  ~  ~  ~  ~|_________________|~  ~  ~  ~  ~  ~  ~  ~
 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
      ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
         '  '  '  '  '  '  '  '  '  '  '  '  '  '  '
'''

# ANSI color codes
YELLOW = "\033[33m"
BLUE   = "\033[34m"
RED    = "\033[31m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def colored_door(color, label):
    return [
        f"{color} __________ {RESET}",
        f"{color}|          |{RESET}",
        f"{color}|  +----+  |{RESET}",
        f"{color}|  |    |  |{RESET}",
        f"{color}|  |    |  |{RESET}",
        f"{color}|  +----+  |{RESET}",
        f"{color}|    ()    |{RESET}",
        f"{color}|          |{RESET}",
        f"{color}|__________|{RESET}",
        f"{color}{BOLD}{label}{RESET}",
    ]

doors = [
    colored_door(YELLOW, "[ yellow ]"),
    colored_door(BLUE,   "[ blue ]"),
    colored_door(RED,    "[ red ]"),
]

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
start = input("Are you ready to start? Type 'yes' or 'no' ").lower()

if start == "yes":
    print(crossroad)
    direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()
    if direction == "left":
        print(island)
        action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
        if action == "wait":
            for row in zip(*doors):
                print("  " + "    ".join(row))
            door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
            if door == "red":
                print("It's a room full of fire. Game Over.")
            elif door == "yellow":
                print("You found the treasure! You Win!")
                print(coin)
            elif door == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")
else:
    print("Maybe next time. Goodbye!")