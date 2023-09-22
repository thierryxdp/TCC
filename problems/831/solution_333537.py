def lingua_p(palavra):
    '''Retorna a palavra onde após suas vogais foram adicionadas um p mais a vogal.
    str -> str'''
    palavra = str.lower(palavra)
    indice = 1
    novo = palavra
    for letra in palavra:
        if letra in 'aeiou':
            novo = novo[0:indice] + 'p'+ letra + novo[indice:]
            indice = indice + 3
        else:
            indice = indice+1

    return novo