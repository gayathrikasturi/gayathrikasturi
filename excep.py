def getAge() :
    retAge = None
    
    for i in range(5) :
        try : 
            age = input("Enter Age : ")
            retAge = int(age)
            print("Age from getAge ", age)
        except :
            print('Invalid input for Age, re-enter ')
        if retAge != None :
            break
    else :
        print("No good input for Age ")
    
    return retAge


age = getAge()
print("Age is ", age)
