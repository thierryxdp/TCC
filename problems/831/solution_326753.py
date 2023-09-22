def lingua_p(palavra):
    'Dada uma palavra, retorna a palavra com a letra p depois de cada vogal. Entrada: str. Saída: str.'
    palavra=str.split(str.join('*',palavra),'*')
    for pos in range(len(palavra)):
        if palavra[pos] in 'AEIOUaeiou':
            palavra[pos]=palavra[pos]+'p'+palavra[pos]
    return str.join('',palavra)