#!/usr/bin/env python
# coding: utf-8

# In[9]:

# found from https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f
def prime_factors(number):
    def add_factor(factors, factor):
        if factor not in factors:
            factors[factor] = 1
        else:
            factors[factor] += 1
    # dictionary mapping prime factor to powers of factor
    prime_factors = {}
    
    # check factors of two and make number odd
    while number % 2 == 0:
        add_factor(prime_factors, 2)
        number //= 2
    
    # check in range [3, sqrt(n)] for factors because we know 
    # that at least one of the factors for a number must be less than sqrt(n)
    # for any non-prime because otherwise if n = p*q where p and q are prime and both 
    # are greater than sqrt(n) then p*q > n
    # Also, we know that we can increment by 2 to only check odds because we already found how many
    # times 2 divides number
    for i in range(3, int(number**0.5)+1, 2):
        
        # check how many times this factor divides number
        while number % i == 0:
            add_factor(prime_factors, i)
            number //= i
    
    # if number > 2 then number is the prime factor of number > sqrt(n)
    if number > 2:
        add_factor(prime_factors, number)
    return [item for item in prime_factors.items()]


# In[ ]:




