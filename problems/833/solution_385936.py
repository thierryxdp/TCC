def conta_numero(numero,m):
    ''' função que retorna a quantidade de vezes um número aparece numa matriz, dados o número desejado e a matriz que será analisada
    int, list --> int'''
    x = 0
    if len(m) == 0:
        return 0
    else:
        numerolinhas = len(m)
        numerocolunas = len(m[0])
        for i in range(len(m)):
            if numero in m[i]:
                x = x+m[i].count(numero)
        return x