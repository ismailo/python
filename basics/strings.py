# Here is an example of using print to display message to the user:
print('Hello, World!')

# Display your own message using print below:
print('Salam, Bros & Siss!')



# Write your function, here.
def concat_name(first_name, last_name):
  return last_name + ", " + first_name

# Here's a version that uses string formatting
def concat_name_f(first_name, last_name):
  return f"{last_name}, {first_name}"


print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"

print(concat_name_f("First", "Last"))  #> "Last, First"
print(concat_name_f("John", "Doe"))    #> "Doe, John"
print(concat_name_f("Mary", "Jane"))   #> "Jane, Mary"



# Write your function, here.
def index_string(string):
    return string[2:-1]


print(index_string("Alchemy"))     #> hem
print(index_string("Ridiculous"))  #> iculou
print(index_string("Serendipity")) #> endipit


