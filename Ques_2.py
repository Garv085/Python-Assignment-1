#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ques 2

#taking inputs
gross_income = float(input('Enter your gross income:  '))
dependents = int(input('Enter the no. of dependents:  '))

#given values
Standard_ded = 10000
Dependent_deduction = 3000

#Applying the operations
taxable_income = gross_income - Standard_ded - (Dependent_deduction * dependents)
income_tax = taxable_income * 0.2

#Display result
print('Income tax person needs to pay = %0.2f' %income_tax)


# In[ ]:




