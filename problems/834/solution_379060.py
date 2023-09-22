def media_matriz(M):
    linha=0
    total=0
    quant=0
    for x in M:
        for i in M[linha]:
           quant=quant+len(M[linha])
            total=total+sum(M[linha])
        linha+=1
    return round(total/quant,2)