def lingua_p(palavra):
    """funcao que recebe de entrada uma palavra (em portugues)
    e retorna esta mesma palavra traduzida para a lingua do P;
    str -> str"""
    
    l_palavra = str.lower(palavra)
    for i in palavra:
        if i in 'aeiouáéíóúâêîôûãõà':
            l_palavra = str.replace(l_palavra, i,i + 'p' + i)
    return l_palavra