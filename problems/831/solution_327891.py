def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna a mesma com
    uma sequência de 'p' após cada vogal.
    str -> str'''
    str.lower(palavra)
    nova_palavra=''
    for i in range(len(palavra)):        
        if palavra[i]  in 'aeiouáéíóúãõÃÕôê':
            nova_palavra = nova_palavra + palavra[i]
        elif palavra[i] not in 'aeiouáéíóúãõÃÕôê':
            nova_palavra= nova_palavra+palavra[i]+'p'
    return nova_palavra