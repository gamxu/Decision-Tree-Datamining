from scipy import linalg
import numpy as np
import math

def entropy(p,n,o):
    if p==0 or n==0 or o==0:
        return (0)
    else:
        _sum = p+n+o
        out = (-p/(_sum))*math.log((p/(_sum)),2) + (-n/(_sum))*math.log((n/(_sum)),2) + (-o/(_sum))*math.log((o/(_sum)),2)
        return(out)

def entropytwo(p,n):
    if p==0 or n==0:
        return (0)
    else:
        _sum = p+n
        out = (-p/(_sum))*math.log((p/(_sum)),2) + (-n/(_sum))*math.log((n/(_sum)),2)
        return(out)
    


def inforD(m,n): 
    c=len(m)
    out=0
    i=0
    for i in range (c):
        out +=(m[i]/sum(m))*n[i]
    return(out)
    

print(entropy(2,3,0))