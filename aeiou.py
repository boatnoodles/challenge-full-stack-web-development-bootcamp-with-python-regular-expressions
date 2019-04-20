# this is how you import a module. we will go through what module means later on. In the meantime, just think of module as a collection of code which typically contains useful functions you can use throughout your code base if you include them in each new file you create (you only need to import a module ones per file).
import re
my_string = "12-34-56"
# we're using the sub method from the re module!
print(re.sub("(\d{2})-\d{2}-(\d{2})", r"\1-**-\2", my_string))

# hello ==> h*ll*
# how are you ==> h*w *r* y**
hello = "hello"
pattern = r"[aeiou]"
print(re.sub(pattern, "*", hello))
# print(re.match("([^aeiou])[aeiou]([^aeiou]{2})[aeiou]", hello))

# hwru = "how are you"
# print(re.sub("([^aeiou])[aeiou]([^aeiou]+)\s([^aeiou]+)[aeiou]+", r"\1"))
# print(re.match("[^aeiou]+", hwru))
