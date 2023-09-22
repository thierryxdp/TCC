def pontos_por_time(lista):
    def jogo(lista):
        dici={lista[0]:0,lista[1]:0}
        if lista[2][0]>lista[2][1]:
            dici[lista[0]]=dici[lista[0]]+3
            return dici
        elif lista[2][0]==lista[2][1]:
            dici[lista[0]]=dici[lista[0]]+1
            dici[lista[1]]=dici[lista[1]]+1
            return dici
        else:
            dici[lista[1]]=dici[lista[1]]+3
            return dici
    a=jogo(lista[0])
    b=jogo(lista[1])
    b[lista[0][0]]=b[lista[0][0]]+a[lista[0][1]]
    b[lista[0][1]]=b[lista[0][1]]+a[lista[0][0]]
    return b