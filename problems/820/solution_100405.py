def posLetra(codigo,letra,ocorrencia):
    """retorna em que posição do codigo aquela ocorrencia da letra esta; str, str, int -> int"""
    a=0
    b=[]
    if str.count(codigo)<ocorrencia:
        return -1
    while a<len(codigo):
        codigo[a]=letra:
            list.append(b,a)
    return b[ocorrencia]