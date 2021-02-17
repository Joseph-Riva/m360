#!/usr/bin/env python
# coding: utf-8

# ## if $n=q*m+r$ then $gcd(n,m) = gcd(m,r)$

# In[1]:


def gcd(a,b, log=True):
    if log:
        print(f'gcd({a},{b})-> {b}={b//a}*{a} + {b%a}')
    if a > b:
        #ensuring the order is correct
        return gcd(b,a,log)
    if a%b == 0 or b%a==0:
        ans=a
        if log:
            print(f'ans->{ans}')
        return ans
    return gcd(b%a, a, log)


# In[2]:


assert gcd(84,108,log=False)==12
assert gcd(108,84,log=False)==12


# LCM can be computed based on the fact that $lcm(a,b)*gcd(a,b)=a*b$ so
# $LCM=\frac{a*b}{gcd(a,b)}$

# In[3]:


def lcm(a,b):
    if a > b:
        return lcm(b,a)
    ab_gcd = gcd(a,b, log=False)
    ab_prod = a*b
    ans = ab_prod// ab_gcd
    print(f'LCM of {a} and {b} is {ans} == {a}*{b}/gcd({a}, {b}) == {ab_prod}/{ab_gcd}')
    return ans


# In[4]:


assert lcm(108,84) == 756


# In[12]:


if __name__ == "__main__":
    gcd(66,81)
    print()
    gcd(119,161)
    print()
    gcd(10385,6633)
    print()
    gcd(589,155)


# In[ ]:




