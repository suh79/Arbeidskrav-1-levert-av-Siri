#!/usr/bin/env python
# coding: utf-8

# """
# <H2>Oppgave 1, Kjøpe bil, elbil eller bensin ? La oss sammenligne kostnadene. 
# Gitt at renter på billån og verditap er det samme i begge tilfellene.</H2>
# <H3>by: suh </Br>
# 2024 10 30</H3>
# """

# In[167]:


C = 10000 # C antall km kjørt 


# In[169]:


FE = 5000  # Forsikring Elbil per år


# In[171]:


FB = 7500  # Forsikring bensinbil pr år


# In[173]:


T = (8.38 * 365)  # Trafikkforsikringsavgift er 8,38 kr pr dag 


# In[174]:


DE = (0.2 * 2 * C)  # Drivstoff el-bil 0,2 kWh pr. km, pris 2,0 kr/kWh


# In[177]:


DB = (1 * C)  # Drivstoff bensinbil 1,0 kr/km 


# In[179]:


BE = (0.1 * C)  # Bomavgift Elbil 0,1 kr/km


# In[180]:


BD = (0.3 * C)  # Bomavgift Bensinbil 0,3 kr/km


# In[183]:


A = (FE + T + DE + BE)


# In[185]:


print("Årlige total kostnader for Elbil er", round(A))


# In[187]:


B = (FB + T + DB + BD)


# In[188]:


print ("Årlige total kostander for bensin bil er", round(B))


# In[191]:


C = (B - A)  # Årlig differanse mellom Elbil og Bensinbil


# In[193]:


print ("Utregningen viser at det lønner seg å handle Elbil kostnadsmessig. Differansen mellom de årlige kostnadene for Elbil og Bensinbil er", round(C))

