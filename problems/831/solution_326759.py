def lingua_p(palavra):
    """..."""
    contador = 0
    for letra in palavra:
        if letra in 'aeiou':
            palavra_nova = palavra[:contador+1]+str(p)+str(letra)+palavra[contador+2:]
            
        contador = contador + 1
    return palavra_nova