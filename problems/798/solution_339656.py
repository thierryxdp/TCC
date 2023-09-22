def freq_palavras(frases):
    '''str -> dict
    plvs armazena uma tupla com cada palavra de frases, ind se refere ao índice
    de cada item em plvs e dic é o dicionário novo'''
    plvs=frases.split()
    ind=0
    dic={}
    while ind<len(plvs):
        if plvs[ind] in dic:
            dic[plvs[ind]]+=1
        else:
            dic[plvs[ind]]=1
        ind+=1
    return dic