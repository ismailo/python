# Write your function, here.
def is_last_character_n(name):
    return name[-1] == "n"


print(is_last_character_n("Aiden"))  #> True
print(is_last_character_n("Piet"))   #> False
print(is_last_character_n("Bert"))   #> False
print(is_last_character_n("Dean"))   #> True