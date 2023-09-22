def lingua_p(texto):
    '''função que, dada uma palavra(texto), retorna a mesma
    palavra traduzida para a lingua do P. Após cada vogal da palavra
    é inseria sequência de letra P. str->str'''
    contador=''
    for i in range(len(texto)):
        if texto[i] in 'aeiouáéíú':
            contador=contador+texto[i]+'p'+texto[i]
        else:
            contador=contador+texto[i]
    return contador