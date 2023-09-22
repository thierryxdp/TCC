def lingua_p(frase):
    """Recebe uma frase e retorna a mesma dentro da língua do p;
    	str -> str"""
    str.lower(frase)
    for i in range(len(frase)):
        if frase[i] in 'aeiou':
            mudar=frase[i]+'p'+frase[i]
            str.replace(frase,frase[i],mudar,i)
    return frase