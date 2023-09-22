def posLetra (texto, letra, numero):
    """dada uma string, letra e numero como entrada, retorna em que posição da string aquela ocorrencia da letra esta, de acordo com o numero de ocorrencia solicitado;
    str,str,int->int."""
    lista=[texto]
    p=0
    newlista=[]
    while p<len(texto):
        if texto[p] == letra:
            newlista=newlista+[p]
        p=p+1
    if len (newlista) < numero:
        return -1
    return newlista[numero-1]