import math
def hashtag(s):
    '''função que recebe uma palavra e insere # no inicio, meio e final'''
 
     i=len(s)
     f=i//2
     
     return "#"+ s[:f]+"#"+ s[f+1:]+"#"