def posLetra(texto,letra,ocorrencia):
    """retorna em que posição do texto a ocorrencia da letra
    aparece. se existirem menos ocorrencias que o pedido, a função retornará -1.
    str,str,int->int"""
    o=0
    i=0
    if letra not in texto:
        return -1
    while o<ocorrencia:
        if texto[i]==letra:
            o=o+1
        else:
            o=o
        i=i+1 
    return o