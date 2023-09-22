def multiplo(x,n):    
    return True  if x%n==0 else False   
def  filtraMultiplos(lista,n):
    list(filter(multiplo(lista,n),lista))
    return