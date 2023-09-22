def posLetra(frase,letra,ocorrencia):
    """retorna a posição da letra na frase 
    str,str,int->str"""
    
    i=1
    
    if ocorrencia>str.count(frase,letra):
        return -1
    else:
        while i<ocorrencia:
            frase=str.replace(frase,letra,'0',1)
            i=i+1
            
        return str.index(frase,letra)