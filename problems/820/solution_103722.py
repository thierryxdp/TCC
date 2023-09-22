def posLetra(frase, letra, n):
    """
    Cóodigo que retorna a poosição de letra na frase
    :frase--> str:
    :letra--> str:
    :n--> int:
    :return--> :
    """
    
    qnt_letras = str.count(frase, letra)
    
    if qnt_letras < n:
        return -1
    else: 
        
        i=0
        p=0
                
        while i<len(frase):            
            p= str.index(frase, letra, n-1)
                            
            i+=1        
        return p