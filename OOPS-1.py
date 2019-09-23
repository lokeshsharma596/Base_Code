class person:
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company
        
    def email(self):
        self.email= self.name + "@" + self.company +".com"
        print(self.email)


e1=person('lokesh',34,'hcl')
e2=person('xyz',54,'poc')

print(e1.name)
print(e2.age)


e1.email()


del e2.name


e2.name="hello"



print(e2.name)


# In[85]:


del e1,e2


class student(person):
    pass


s1=student('lok',67,'goog')


print(s1.name ,s1.age,s1.company)
s1.email()



##adding __init__ to child

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.



class student(person):
    def __init__(self,name,age,company):
        pass


class student(person):
    def __init__(self,name,age,company):
         person.__init__(self, name, age,company)

