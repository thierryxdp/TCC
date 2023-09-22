#str -> dicts
def freq_palavras(frases):
    #criar o dicionário e separar a string em palavras
    partes=frases.split()
    dic={}
    limite=0
    #acrescentar cada palavra no dicionário e seus valores
    while limite!=len(frases):
        if partes[limite] in dic:
            dic[partes[limite]]+=1
        else:
            dic[partes[limite]]=1
        limite+=1
        
    return dic