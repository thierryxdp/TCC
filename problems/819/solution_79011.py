def multiplo(x,n):
    return True  if x%n==0 else False   
def  filtraMultiplos(lista,n):
        return list(filter(multiplo(x,n),lista