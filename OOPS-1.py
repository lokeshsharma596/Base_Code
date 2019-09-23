#!/usr/bin/env python
# coding: utf-8

# # Class and Object:

# In[78]:


class person:
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company
        
    def email(self):
        self.email= self.name + "@" + self.company +".com"
        print(self.email)


# In[79]:


e1=person('lokesh',34,'hcl')
e2=person('xyz',54,'poc')


# In[80]:


print(e1.name)
print(e2.age)


# In[81]:


e1.email()


# In[82]:


del e2.name


# In[83]:


e2.name="hello"


# In[84]:


print(e2.name)


# In[85]:


del e1,e2


# # Inheritance:

# In[93]:


class student(person):
    pass


# In[94]:


s1=student('lok',67,'goog')


# In[95]:


print(s1.name ,s1.age,s1.company)
s1.email()


# In[101]:


##adding __init__ to child

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.


# In[104]:


class student(person):
    def __init__(self,name,age,company):
        pass


# In[106]:


class student(person):
    def __init__(self,name,age,company):
         person.__init__(self, name, age,company)

