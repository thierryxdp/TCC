def uppCons (frase):
    """Recebe uma frase, e retorna a frase original com
    todas as consoantes em maiúsculas, e os outros carateres
    inalterados, todos na posição original.
    str -> str"""
    indice = 0
    nova_frase = ' '
    while indice < len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            nova_frase += str.upper(frase[indice])
        else:
            nova_frase += frase[indice]
        indice += 1
    return nova_frase