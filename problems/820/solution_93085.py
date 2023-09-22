def posLetra(string,letra,numero):
    """Essa função retorna a ocorrência pedida da letra informada
    dentro da string, caso essa ocorrencia se encontre fora da ocorrência
    da letra ele retorna o valor -1. Como entrada temos uma string,uma letra
    e um número. Como saída temos o número da ocorrência pedida;
    str,str,int->int"""
    indice=0
    contagem=str.count(string,letra)
    posicao=[]
    if contagem<numero:
        posicao=-1
        return posicao
    else:
        while indice<len(string):
            if string[indice]==letra:
                posicao=posicao+[string.find(letra,indice),]
            indice+=1
    i=posicao[numero-1]
    return i