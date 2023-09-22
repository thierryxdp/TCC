def lingua_p(palavra):
    """Funcao que traduz uma palavra para lingua do P;
    Entrada: str
    Saida: str"""
    
    palabra=str.lower(palavra)
    
    for i in range(palavra):
        if palavra[i] in 'aeiouáàãâéêiíîoóõuú':
            palabra[i]+='p'+palabra[i]
    return palabra