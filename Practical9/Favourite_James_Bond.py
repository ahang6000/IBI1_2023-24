def fav_JB(year):
    if year+18<=1986 and year+18>=1973:
        return "Roger Moore"
    elif year+18<=1994 and year+18>=1987:
        return "Timothy Dalton"
    elif year+18<=2005 and year+18>=1995:
        return "Pierce Brosnan"
    elif year+18<=2021 and year+18>=2006:
        return "Daniel Craig"
    else:
        return"no one. Sorry, we don't have sufficient information about James Bond in your era."

year=int(input("Please enter your year of birth:"))
print("Your favourite James Bond might be",fav_JB(year))
#example
print("example:")
print("I was born in 1985, so my favourite James Bond actor is",fav_JB(1985),"according to the theory.")
#the output shows "I was born in 1985, so my favourite James Bond actor is Pierce Brosnan."