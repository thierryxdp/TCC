def uppCons(frase):
    maiuscula= frase
    proximo=0
    while proximo < len(frase):
        if frase[proximo] in "BCDFGHJKLMNPQRSTVXZWYÇbcdfghjklmnpqrstvxzwyç":
            maiuscula=maiuscula.replace(frase[proximo],str.upper(frase[proximo]))
        proximo = proximo+ 1
    return maiuscula