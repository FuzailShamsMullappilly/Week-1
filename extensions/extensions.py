ext=str.strip(str.lower(input("File name: ")))
if ext.endswith(".gif"):
    print("image/gif")
elif ext.endswith(".jpg"):
    print("image/jpeg")
elif ext.endswith(".jpeg"):
    print("image/jpeg")
elif ext.endswith(".png"):
    print("image/png")
elif ext.endswith(".pdf"):
    print("application/pdf")
elif ext.endswith(".txt"):
    print("text/plain")
elif ext.endswith(".zip"):
    print("application/zip")
elif ext.endswith(".bin"):
    print("application/octet-stream")
else:
    print("application/octet-stream")
