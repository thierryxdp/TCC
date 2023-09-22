def uppCons(frase):
    """ transforma em maisculo somente as consoantes de uma frase, retornando
    a frase com as mudanças feitas;str->str"""
    resposta=[]
    indice=0
    while(indice<len(frase)):
        if (str.lower(frase[indice]) not in "aeiouáéíóúâêîôûãõ"):
            list.append(resposta, str.upper(frase[indice]))
        else:
            list.append(resposta, frase[indice])
        indice+=1
    return str.join("", resposta)