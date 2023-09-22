#str -> dicts
def freq_palavras(frases):
    #criar o dicionário e separar a string em palavras
    partes=frases.split()
    dic={}
    limite=0
    #acrescentar cada palavra no dicionário e seus valores
    while limite!=len(frases):
        if partes[tam] in dic:
            dic[partes[tam]]+=1
        else:
            dic[partes[tam]]=1
        limite+=1
        
    return dic