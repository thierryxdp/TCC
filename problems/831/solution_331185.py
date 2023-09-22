def lingua_p(palavra:str)->str:
    """Recebe palavra em português e retorna a mesma traduzida para a língua do P."""
    tradu=[palavra]
    for i in range(palavra):
        if palavra[i] in 'AEIOUaeiou':
            tradu.insert(i+1,'p'+palavra[i])
    return str(tradu)