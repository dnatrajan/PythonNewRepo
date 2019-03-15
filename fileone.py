def func():
	print("Function running in fileone.py")
	
print("Top level print inside fileone.py")

if __name__=="__main__":
	print("Fileone.py is being rund directly")	
else:
	print("Fileone.py is being imported into another module")