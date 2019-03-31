import random

pachikona_menu = {
    "chips": ["$3 dollars,fried  with spices and tomato sauce"],
    "fish and chips": ["$4 dollars,plus free drink "],
    "rice and chicken": ["$5 dollars, plus one free piece"],
    "hot noodles": ["$2 dollars, cooked chinese style"],
    "beef burger": ["$2 dollars,served with chilledd lemonade "]}


def intro():
  print('Welcome to DOUBLES RESTURANT.WOUlD YOU LIKE TO LOOK AT THE MENU:')

  choice = input("Yn").lower()
  if choice != 'n':
      for names in pachikona_menu:
        print(names)


def main():
    intro ()
    print ("select your food?")
    name = str (input ()).lower ()
    if name == "chips".lower ():
        for info in pachikona_menu["chips"]:
            print (info)
    elif name == "fish and chips".lower ():
        for info in pachikona_menu["fish and chips"]:
            print (info)
    elif name == "rice and chicken".lower ():
        for info in pachikona_menu["rice and chicken"]:
            print (info)
    elif name == "hot noodles".lower ():
        for info in pachikona_menu["hot noodles"]:
            print (info)
    elif name == "beef burger".lower ():
        for info in richest_pple_in_the_wrld["beef burger"]:
            print (info)
    else:
        print ("SORRY NOT ON OUR MENU TODAY")

    main ()


main ()