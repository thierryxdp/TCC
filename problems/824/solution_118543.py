def uppCons(frase):
    """essa função recebe uma frase como parametro e retorna a mesma com todas as letras consoantes maiusculas
    list->list"""
    maiuscula= frase
    proximo=0
    while proximo < len(frase):
        if frase[proximo] in "BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy":
            maiuscula=maiuscula.replace(frase[proximo],str.upper(frase[proximo]))
        proximo = proximo+ 1
    return maiuscula