# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 07:47:25 2016

@author: PR
"""


       
    
    
def separation_pos_neg(seq):
    """separation takes a tuple and return a list containing a positive list 
    a negative list"""
    seq_pos = []
    seq_neg = list(seq)
    for i in range(len(seq)):
        if seq[i] > 0:
            seq_pos.append(seq[i])
            seq_neg.remove(seq[i])
    return seq_pos , seq_neg
            


def rearrange(cond_conv_seq,beta):
    """rearrange yields a sequence of the conditional convergent serie 
    such that its sum is equal to beta"""
    seq = list(cond_conv_seq)   
    seq_pos , seq_neg = separation_pos_neg(seq)
    print(seq_pos,seq_neg)
    sum_seq = seq[0]     
    i = 0           # i is used as index for positive elements
    j = 0           # j is used as index for negative elements
    if sum_seq > 0.:     # adjust i or j depending on the sign of the first element 
        i = 1
    elif sum_seq <= 0.:
        j = 1               
    while (sum_seq != beta) == True:
        if sum_seq < beta:
            sum_seq += seq_pos[i]
            i += 1
            yield seq_pos[i-1]
        elif sum_seq > beta:
            sum_seq += seq_neg[j]
            j += 1
            yield seq_neg[j-1]
        elif sum_seq == beta:
            break
            
    
            
def test_rearrange(cond_conv_seq, error):
    """test_rearrange picks a random float beta and returns True if after 
    some finite number of steps N, the difference between the absolute value 
    of the sum of the generator rearrange and beta is smaller then error"""
    import random
    beta = random.random()
    seq = rearrange(cond_conv_seq,beta)
    N = 1000
    j = 0
    sum_seq = 0
                
    for i in seq:
         while j < N :
             sum_seq +=i
             if abs(beta - sum_seq) < error : 
                 return True
             j += 1 
         return False
           
            
def cond_conv_seq():
    """ Generates (-1)^(n+1)/n. """
    n = 1.
    sign = 0
    while True :
        yield (-1)**sign/n
        n += 1.
        sign = 1 - sign
            
            
            
            
            
    