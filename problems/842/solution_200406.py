def pontos_por_time(lista):
    """Função que calcula e diz qual foi o time vencendor dado 1 lista
    com 2 elementos e, cada elemento é uma outra lista.
    list, list -> dict"""
    nome1 = lista[0][0]
    nome2 = lista[1][0]
    ponto1 = int(lista[0][2][0])
    ponto2 = int(lista[0][2][1])
    ponto3 = int(lista[1][2][0])
    ponto4 = int(lista[1][2][1])
    
    if ponto1>ponto2 and ponto3<ponto4:
        return {nome1:6, nome2:0}
    if ponto1>ponto2 and ponto3==ponto4 or ponto1==ponto2 and ponto3<ponto4:
        return {nome1:4, nome2:1}
    if ponto1==ponto2 and ponto3==ponto4:
        return {nome1:2, nome2:2}
    if ponto1<ponto2 and ponto3>ponto4:
        return {nome1:0, nome2:6}
    if ponto1<ponto2 and ponto3==ponto4 or ponto1==ponto2 and ponto3>ponto4:
        return {nome1:1, nome2:4}
    if ponto1>ponto2 and ponto3>ponto4:
        return {nome1:3,nome2:3}