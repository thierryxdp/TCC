def lingua_p(frase):
    """Recebe uma frase e retorna a mesma dentro da língua do p;
    	str -> str"""
    str.lower(frase)
    for i in range(len(frase)):
        if frase[i] in 'aeiou':
            mudar=frase[i]+'p'+frase[i]
            frase=str.replace(frase,frase[i],mudar,i)
            i=i+2
    return frase