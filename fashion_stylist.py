import random

top = ["halter top", "polo shirt", "tank top", "basketball jersey", "fitted bodice", "concert t-shirt", "college sweatshirt", "knit sweater", "denim jacket"]
bottom = ["bell-bottoms", "capri pants", "mom jeans", "cargo shorts", "a tutu", "glittery leggings", "acid-washed jeans", "a pencil skirt", "a ball gown", "a kilt", "sailor pants", "a boho skirt"]
accessory = ["nose ring", "scrunchie", "set of bangles", "slap bracelet", "spiked collar", "pair of diamond earrings", "tiara", "fake tattoo", "top hat", "beret", "newsboy cap", "choker", "fake beauty mark"]
footwear = ["Doc Martens", "Birkenstocks", "flip-flops", "Mary Janes", "stilettos", "skater shoes", "Keds", "platform shoes", "cowboy boots", "gladiator sandals", "high heels", "Air Jordans"]
compliment = ["Stunning!", "Gorgeous!", "Too cool!", "Breathtaking!", "Phenomenal!", "Cover-worthy!", "Unbelievably chic!", "Striking!", "Daring!"]

name = input("Hi. What's your name? ")
days = int(input("How many days of outfits should I plan for you? "))

if days == 0:
    print ("Bummer, I was looking forward to styling you.")

else: 
    print("Here's a schedule of outfits that'll look fab on you, " + name + "! ")

    for x in range(0,days): 
        print("Day " + str(x + 1) + ":  A " + random.choice(top) + " over " + random.choice(bottom) 
        + "! Add a " + random.choice(accessory) + ", throw on a pair of " + random.choice(footwear) + ". " + random.choice(compliment))


