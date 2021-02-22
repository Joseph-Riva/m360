#!/usr/bin/env python
# coding: utf-8

# In[7]:


from scripts.factor import prime_factors
def phi(n):
    factors = prime_factors(n)
    ret=1
    for prime_factor, power in factors:
        ret *= phi_prime(prime_factor, power)
    return ret

# phi(p**k) where p is prime == p**k -p**(k-1)
def phi_prime(p, power):
    return p**power - p**(power-1)

# In[8]:
def num_prim(p):
    return phi(p-1)
assert phi(420) == 96


# In[ ]:




