#str -> dicts
def freq_palavras(frases):
    #criar o dicionário e separar a string em palavras
    partes=frases.split()
    dic={}
    lim=0
    #acrescentar cada palavra no dicionário e seus valores
    while lim!=len(frases):
        if partes[lim] in dic:
            dic[partes[lim]]+=1 
            lim=lim+1
        else:
            dic[partes[lim]]=1
            lim+=1
        
    return dic