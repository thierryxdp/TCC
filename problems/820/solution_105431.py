def posLetra(string,letra,numero):
    i=0
    ocorrencia=0
    if str.count(string,letra)<numero or letra not in string:
            return -1
    else:
        while str.count(string,letra)=>numero:
            if string[i]==letra:
                posicao=i
        return posicao