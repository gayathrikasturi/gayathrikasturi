def add(*l) :
    sum = 0
    global test
    test=200
    print("test from add",test)
    for e in l :
        sum += e
    return sum

test = 100

print("from calclib3 : ", __name__)
if __name__=="__main__":
	print("test",test)
	r=add(1,2,3,4)
	print("test after add",test)
	print(r)