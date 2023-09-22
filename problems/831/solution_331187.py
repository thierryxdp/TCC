def lingua_p(palavra:str)->str:
    """Recebe palavra em português e retorna a mesma traduzida para a língua do P."""
    palavra=list(palavra)
    i=0
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            palavra.insert(i,'p')
    return str.join('',palavra)