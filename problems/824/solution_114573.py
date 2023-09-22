def uppCons(frase):
    maiuscula=''
    proximo=0
    while proximo <= len(frase):
        if frase[proximo] in "BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy":
            maiuscula=maiuscula+str(frase[proximo]).upper
        proximo= proximo+1
    return maiscula