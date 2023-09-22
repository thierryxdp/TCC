def posLetra(palavra,letra,n):
    '''A funcao recebe uma sentenca, uma letra e uma ocorrencia e retorna qual o indice
da enesima ocorrencia dessa letra str,str,int->int'''   
    x=palavra.replace(letra,'θ',n-1)
    return x.index(letra)