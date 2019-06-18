class students:

	 def __init__(self,name,contact):
	 	self.name=name
	 	self.contact=contact 
	 def getdata(self):
	 	 self.name=input("enter the name")
	 	 self.contact=input("enter contact")
	 def putdata(self):
	 	 print("name is:"+self.name)
	 	 print("contact:"+self.contact)
class teacher(students):
      def __init__(self,age):
         self.age=age

      def getage(self):
         print("age is done")



g=teacher(0)
g.getage()
g.getdata()
g.putdata()
