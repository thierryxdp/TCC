def uppCons(texto):
    lista_texto = list(texto)  #quebra a string texto e coloca em uma lista
    contador = 0 #inicia o contador 
    letras = []  #abre uma lista vazia    

    while contador < len(lista_texto):
        if lista_texto[contador] in 'bcdfghjklmnpqrstvwxyz':
            letras.insert(contador, lista_texto[contador].upper())
            
            contador = contador + 1
            
        elif lista_texto[contador] in 'aeiou':
            letras.insert(contador, lista_texto[contador])
            
            contador = contador + 1

        else:
            letras.insert(contador, lista_texto[contador])

            contador = contador + 1

    return ''.join(letras)