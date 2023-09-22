def uppCons(texto):
    lista_texto = list(texto)
    contador = 0
    letras = []
    
    while contador < len(lista_texto):
        if lista_texto[contador] in ’bcdfghjklmnpqrstvwxyz’:
            letras.insert(contador, lista_texto[contador].upper())
            contador = contador + 1
            
        else:
            letras.insert(contador, lista_texto[contador])
            contador = contador + 1
            
    return ’’.join(letras)