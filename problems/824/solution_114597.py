def uppCons(frase):
    '''a função recebe uma frase e retorna a mesma frase com as
    consoantes maiusculas
    str->str
    '''
    maiuscula= frase
    proximo=0
    while proximo < len(frase):
        if frase[proximo] in "BCDFGHJKLMNPQRSTVXZWYÇbcdfghjklmnpqrstvxzwyç":
            maiuscula=maiuscula.replace(frase[proximo],str.upper(frase[proximo]))
        proximo = proximo+ 1
    return maiuscula