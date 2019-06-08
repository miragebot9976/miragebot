import random

def roll_dice(num_dice = 3,num_sides = 6):
    output = ""
    sum = 0
    for i in range(num_dice):
        roll = random.randint(1,num_sides)
        sum += roll
        output += "{}/6 ".format(roll)
    output += "Total: {}".format(sum)
    return output

def payout(num_people, num_vg, num_thermite):
    payout = (int(num_vg) * 8000) / int(num_people)
    cost = (int(num_thermite) * 3000) / int(num_people)
    if int(num_people) > 1:
        supplier = payout + cost * (int(num_people) - 1)
        rest = payout - cost
        supplier = supplier/1000
        rest = rest/1000
    else:
        supplier = payout - cost
        supplier = supplier / 1000
        rest = 0

   
    output = [supplier, rest]
    return output