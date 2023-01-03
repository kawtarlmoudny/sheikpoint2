#!/usr/bin/env python
# coding: utf-8

# In[7]:


firstname = input("enter your first name:")
lastname = input("enter your last name:")
name1 = firstname[::-1]
name2 = lastname [::-1]
print(name1,"",name2)


# In[15]:


n=5
z=0
for i in range (3):
    result= str(n)*(i+1)
    z= z+ int(result)
print(z) 


# In[19]:


x =input("write a number:")
if int(x)%2==0:
    print("this number is even")
else:
    print("the number is odd")


# In[22]:


for i in range (2000,3201):
    if i%7==0 and i%5!=0:
        print(i)


# In[27]:


x=input()
result=1
for i in range (int(x)):
    result=result*(i+1)
print(x,"!=",result)    


# In[29]:


n="hello team"
f=""
for i in range (0,len(n)):
    if i%2==0:
        f=f+n[i]
print(f)


# In[31]:


price=int(input())
disc=1
if price>=500:
    disc=disc-0.5
    disc*=price
elif price>=200:
    disc=disc-0.3
    disc*=price
print(disc)    


# In[ ]:




