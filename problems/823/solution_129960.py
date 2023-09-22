def faltante(lista):
    """função que retorna a peça que está faltando; list-> """
    i=0
    j=0
    k=0
    nova= []
    while i<len(lista):
        nova[i]=0
        i+=1
        
    while k<len(nova)-1:
        nova[lista[k]]=1
        
    while j <len(nova)-1:
        if nova[j]==0:
    		return j