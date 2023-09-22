def uppCons(frase):
    
    """Funçao que calcula e retorna uma frase com todas
    suas consoantes em maísculo a partir de uma frase dada."""

    lista = list(frase)
    
    i = 0
    
    while i < len(lista):
        
        if lista[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            
            lista[i] = str.upper(lista[i])
            
        i = i + 1
        
    return ''.join(lista)