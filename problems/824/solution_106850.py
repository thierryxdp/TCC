def uppCons(frase):
    
    """Essa funcao retorna a mesma frase dada como entrada, mas com as consoantes em letras maiusculas;
    str -> str"""
    
    nova_frase = ''
    i = 0

    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUáéíóÁÉÍÓãõÃÕ':
            maiuscula = str.upper(frase[i])
            nova_frase = nova_frase + maiuscula
        if frase[i] in 'aeiouAEIOUáéíóÁÉÍÓãõÃÕ':
            nova_frase = nova_frase + frase[i]
        i = i + 1
    return nova_frase