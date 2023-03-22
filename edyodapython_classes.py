#!/usr/bin/env python
# coding: utf-8

# In[15]:


a=34
b='3.4'
print('after typcasting')
b=float(b)
print(a+b)


# In[7]:


ls1=[]
ls2=["mango","apple","papaya"]

ls1.append(ls2)
ls2.append("pomegrenate")

print(ls1)


# In[8]:


a=[]
b=input("Enter the values  of the list: ")
a=b.split(",")
print(a)

#why it is not spliting?


# a=[]
# b=input("Enter the values of the list")

# In[38]:


l=["1","2","31","34","22"]
print("+".join(l))

    


# In[2]:


l=['1','2','3']

l.append(5)
print(l)


# In[16]:



a=(input("Enter your roll no.: "))
print("this is my roll no.",int(a))

l=[]

for i in a:
    
    l.append(i)
    print(l)
    print(i)


# In[21]:


a=1.3
print(id(a))
a=2.4
print(id(a))


# In[8]:


course = "some examples of python program"
#split of the line into list of words
print(course[0])
print(len(course))
a=course.split(" ")
print(a[-1])#last word
print(a[0])#first word
print(len(a))
print(a)


# In[13]:


a="welcome to edyoda classes"
print(len(a))
b=a.split()
print(b)
print(b[0])
print(len(b))


# In[17]:


n=input()
sets=set(n)
print(sets)
nr=str(sets)
print(nr)


# In[22]:


#int,float,string are immutable there memory locATION will be different

a="3,4"
print(id(a))
a="2.3"
print(id(a))


# In[26]:


a=[]
print(id(a))
b=[]
print(id(b))


# In[ ]:





# In[ ]:




