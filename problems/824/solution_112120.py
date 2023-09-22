def uppCons(frase):
    a=str.upper(frase)
    subV=['A','E','I','O','U']
    subN=['a','e','i','o','u']
    fpartida= str.split(a)
    b=str.replace(a,subV,subN)
    
    
    
    return b