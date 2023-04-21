#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## [Optional] Challenge activity: Create a dictionary

# **This is the solution to the activity.**
# 
# You are employed by InputDat, a data analytics consulting firm. The Brazilian government Department of Environment and Wildfires wants to determine the extent of wildfire damage to indigenous forests, forest plantations, and human settlements.
# 
# You have been provided with a list of states in Brazil and their respective capitals. Your manager needs you to create a Python dictionary object containing the name of each state and its capital so that analysis on the wildfires is easier to conduct. Your dictionary will be leveraged by other analysts at InputData when they continue the analysis.
# 
# You will utilise the `Brazilian-states-and-capitals.csv` file that was included in the ZIP file you downloaded from 1.0 Focus of the week. Create a dictionary object containing the name of each state and its capital.

# ## List of the Brazilian states 

# In[ ]:


states = ['Acre', 'Alogoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Distrito Federal', 
          'Espirito Santo', 'Goiás', 'Maranhao', 'Mato grosso', 'Mato grosso do sul', 
          'Minas gerais', 'Para', 'Paraiba', 'Parana', 'Pernambuco', 'Piaui', 'Rio de Janeiro', 
          'Rio Grande do norte', 'Rio Grande do Sul', 'Rondonia', 'Roraima', 'Santa Catarina', 
          'Sao Paulo', 'Sergipe', 'Tocantins']


# ## List of the Brazilian capitals 

# In[ ]:


capitals = ['Rio Branco', 'Maceió' 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 
            'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém',
            'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 
            'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 
            'Aracaju', 'Palmas']


# ## Dictionary of the Brazilian states and their capitals 
# 
# (NOTE: We have only provided you with the first five states. You will need to complete the dictionary by keying in the rest of the states and their capitals.)

# In[ ]:


brazil = {'Acre': 'Rio Branco',
          'Alogoas': 'Maceió',
          'Amapa': 'Macapá',
          'Amazonas': 'Manaus',
          'Bahia': 'Salvador',
          'Ceara': 'Fortaleza',
          'Distrito Federal': 'Brasília',
          'Espirito Santo': 'Vitória',
          'Goiás': 'Goiânia',
          'Maranhao': 'São Luís',
          'Mato grosso': 'Cuiabá',
          'Mato grosso do sul': 'Campo Grande',
          'Minas gerais': 'Belo Horizonte',
          'Para': 'Belém',
          'Paraiba': 'João Pessoa',
          'Parana': 'Curitiba', 
          'Pernambuco': 'Recife', 
          'Piaui': 'Teresina', 
          'Rio de Janeiro': 'Rio de Janeiro', 
          'Rio Grande do norte': 'Natal', 
          'Rio Grande do Sul': 'Porto Alegre', 
          'Rondonia': 'Porto Velho', 
          'Roraima': 'Boa Vista', 
          'Santa Catarina': 'Florianópolis', 
          'Sao Paulo': 'São Paulo', 
          'Sergipe': 'Aracaju', 
          'Tocantins': 'Palmas'}


# In[ ]:


print(brazil)


# ## Codes to return the capitals for Amazonas, Goiás, and Rio de Janeiro

# In[ ]:


brazil ['Amazonas']


# In[ ]:


brazil ['Goiás']


# In[ ]:


brazil ['Rio de Janeiro']


# ## Length of the dictionary

# In[ ]:


print("len() method :", len(brazil))


# In[ ]:




