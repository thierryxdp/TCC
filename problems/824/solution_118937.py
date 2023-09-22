def uppCons(texto):
    '''Recebe uma frase (texto) e retorna a 
    frase com todas as consoantes em maiúsculas
    
    str -> str
    '''
    
    lista_text = list(texto)
    contador = 0
    letras = []
    
    while contador < len(lista_texto):
        if lista_texto[contador] in 'çbcdfghjklmnpqrstvwxyz'  nb :
   			letras.insert(contador, lista_texto[contador].upper())
   			contador = contador + 1
                                                
        else: 
        	letras.insert(contador, lista_texto[contador])
            contador = contador + 1
    return ' '.join(letras)