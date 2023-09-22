def lingua_p(palavra: str) -> str:
    """comentário"""
    
     palavra = list(palavra.lower())
    i=0
    for x in palavra:
        if x in 'aãâáéeêiíoõuú':
            soma_string = 'p'+x
            palavra.insert(palavra.index(x, i)+1, soma_string)
        i+=1
    final = ''.join(palavra)
    return final