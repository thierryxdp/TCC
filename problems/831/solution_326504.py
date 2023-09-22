def lingua_p(palavra):
    """Funcao que traduz uma palavra para lingua do P;
    Entrada: str
    Saida: str"""
    
    palabra=list(str.lower(palavra))
    
    for i in range(len(palabra)):
        if palavra[i] in 'aeiouáàãâéêiíîoóõuú':
            palabra[i]+='p'+palabra[i]
    return str.join(' ',palabra)