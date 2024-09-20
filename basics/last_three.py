def last_three(str, letters):
  return str[-3:].lower() == letters.lower()


print(last_three("Power", "wer"))  #> True
print(last_three("Application", "App"))   #> False
print(last_three("Raw", "raw"))   #> True
print(last_three("Bonjour", "OUR"))   #> True