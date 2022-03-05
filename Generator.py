# Nitro Generator

import string 
import random

def gen(t=16, car=string.ascii_letters + string.digits):
    return ''.join(random.choice(car) for _ in range (t))

nombres=int(input("Nombre de nitro a génerer :")) 

for _ in range(nombres):
    discord = "discord.gift"
    nitro = gen()
    with open("Nitros.txt", "a+") as f:
        f.write(discord)
        f.write("/" + nitro + "\n")