#This program greets the user and 
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively

greating=str.lower(str.strip(input("Greetings: ")))
if greating.startswith("hello"):
    print("$0")
elif greating[0] == "h":
    print("$20")
elif greating[0] != "h":
    print("$100")