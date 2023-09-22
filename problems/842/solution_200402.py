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
    emp= 1
    emp2=2
    if ponto1>ponto2 and ponto3<ponto4:
        return {nome1:6, nome1:0}
    if ponto1>ponto2 and ponto3==ponto4:
        return {nome1:4, nome1:emp}
    if ponto1==ponto2 and ponto3<ponto4:
        return {nome1:4, nome1:emp}
    if ponto1==ponto2 and ponto3==ponto4:
        return {nome1:emp2, nome1:emp2}
    if ponto1<ponto2 and ponto3>ponto4:
        return {nome1:0, nome1:6}
    if ponto1<ponto2 and ponto3==ponto4:
        return {nome1:emp, nome1:4}
    if ponto1==ponto2 and ponto3>ponto4:
        return {nome1:emp, nome1:4}