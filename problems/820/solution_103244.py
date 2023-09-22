def posLetra (string,letra,n):
    '''função que recebe como entrada uma str,uma letra e um 
    número. Essa função retorna em que ocorrencia(N) da str a
    letra está;str->int'''
    resposta=''
    rodada=0
    while rodada<len(string):
        if letra in string:
            resposta+=string[n]
            resposta+=str.find(string,resposta)
        rodada+=1
    return resposta