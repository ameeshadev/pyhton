# printing a message for not visible front end its running back end code
name = input("Enter your name: ")

msg = ''.join(chr(x) for x in [73,32,108,111,118,101,32,121,111,117])

print(msg, "❤️", name)
