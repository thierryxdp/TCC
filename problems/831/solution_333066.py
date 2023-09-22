def lingua_p(palavra):
    '''funcao que recebe uma palavra e retorna a mesma palavra traduzida para a lingua do P
    str->str'''
    minuscula = palavra.lower()
    novaP = ''
    vog = 'aeiouãáéíóú'
    for p in minuscula:
        novaP += p
        if p in vog:
            novaP += 'p' + p
    return novaP