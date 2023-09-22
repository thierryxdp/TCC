def lingua_p(frase):
    """Recebe uma frase e retorna a mesma dentro da língua do p;
    	str -> str"""
    str.lower(frase)
    for i in range(len(frase)):
        if i in 'aeiou':
            mudar=i+'p'+i
            str.replace(frase,i,mudar,frase[i])
    return frase