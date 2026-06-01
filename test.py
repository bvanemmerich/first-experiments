def printgreaterthan4(x,y):
	if x>y:
		print("x is greater than y")

def add(x,y):
	return x+y

print("hello world")
a=2
print(a)
b=add(a,a)
print(b)
if a>4:
	print("a is greater than 4")
else:
	print ("a is less than 4")

for i in range(0, 10):
	print (i)
	b=add(a,b)
	print (b)
	printgreaterthan4(i,7)