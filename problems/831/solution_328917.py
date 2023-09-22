def lingua_p(palavra):
    """
    	Retorna a palavra inserida na língua do P
        str -> str
    """
    palavra.lower()
    palavra_P=palavra
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóúàèìòùâêîôûãõ':
            palavra_P.replace(palavra[i],palavra[i]+'p'+palavra[i])
    return palavra_P