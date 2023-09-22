def lingua_p(palavra):
    """Traduz uma palavra do português para a "língua do P"; str -> str"""
    
    lista_letras = []
    contador = 0
    
    for letra in palavra:
        list.append(lista_letras, letra)

    for item in lista_letras:
        if item in 'AEIOUaeiouáéíóú':
            list.insert(lista_letras, contador + 1,'p' + item)
        contador = contador + 1
        
    return str.lower(str.join('', lista_letras))