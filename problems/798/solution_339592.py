#str -> dicts
def freq_palavras(frases):
    #criar o dicionário e separar a string em palavras
    partes=frases.split()
    dic={}
    #acrescentar cada palavra no dicionário e seus valores
    for tam in range(len(partes)):
        if partes[tam] in dic:
            dic[partes[tam]]+=1
        else:
            dic[partes[tam]]=1 
        
    return dic