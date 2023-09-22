def uppCons(frase):
    """Recebe uma frase e retorna a mesma frase porém com as letras consoantes em letra maiuscula;
    	str -> str"""
    indice=0
    parador=len(frase)-1
    while indice<=parador:
        if frase[indice] in 'qwrtypsdfghjklçzxcvbnm':
            str.replace(frase,frase[indice],str.upper(frase[indice]))
        indice=indice+1
    return frase