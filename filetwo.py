import fileone
print("Top level in flietwo.py")

fileone.func()

if __name__=="__main__":
	print("Two.py is being executed directly")
else:
	print("Filetwo.py is being imported into another module")