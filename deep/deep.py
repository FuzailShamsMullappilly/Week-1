x=input("What is the Snswer to the Great Question of Life, the Universe and Everything?")
x=x.lower()
x=x.strip()
if x=="42":
    print("Yes")
elif  x=="forty two":
    print("Yes")
elif  x=="forty-two":
    print("Yes")
else:
    print("No")
