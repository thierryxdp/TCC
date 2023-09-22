def lingua_p(string):
    """transforma uma palavra em português e uma palavra na lingua do P;str->str"""
    lista= str.strip(string)
    resposta=[]
    for letra in lista:
        if letra in "aeiouAEIOUáéíóú":
            list.append(resposta,str.join(" ",[letra,"p",letra]))
        else:
            list.append(resposta,letra)               
    return str.join(" ", resposta).replace(' ','')