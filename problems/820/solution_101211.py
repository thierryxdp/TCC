def posLetra(texto,letra,ocorrencia):
    """retorna em que posição do texto a ocorrencia da letra
    aparece. se existirem menos ocorrencias que o pedido, a função retornará -1.
    str,str,int->int"""
    o = 0
    i = 0
    while o<ocorrencia or not o==-1:
        if texto[i]==letra:
            o=o+1
        elif texto[i]!=letra:
            o=o
        elif letra not in texto:
            o=-1
        i+=1
    return o