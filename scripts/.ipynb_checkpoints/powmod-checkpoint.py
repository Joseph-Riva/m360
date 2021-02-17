#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pow_mod(base, exp, p=1, b=1, log=False):
    '''computes base**exp % p'''
    if log:
        print(f'pow_mod(base={base},exp={exp},b={b},p={p})')
        
    if exp==1:
        ans = base*b % p
        if log:
            print(f'done->{ans}')
        return ans
    elif exp%2==0:
        return pow_mod(base**2 % p, exp//2, p, b, log)
    #log if odd
    if log:
        print(f'pow_mod(base={base},exp={exp-1},b={base*b},p={p})\t odd')
    return pow_mod(base**2 % p, (exp-1)//2, p, base*b % p, log)


# In[3]:


assert pow_mod(6,50,251, 1) == 219


# In[6]:


if __name__=="__main__":
    ##8**125 % 251
    pow_mod(3,10,1,11)
    print()
    pow_mod(7,49,1,31)


# In[ ]:




