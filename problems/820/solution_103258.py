def posLetra (string,letra,n):
    '''função que recebe como entrada uma str,uma letra e um 
    número. Essa função retorna em que ocorrencia(N) da str a
    letra está;str->int'''
    resposta=''
    resposta2=''
    rodada=0
    while rodada<len(string):
        if letra in string:
            resposta=str.find(string,string[n])
            resposta2=str.count(string,resposta)
        rodada+=1
    return resposta2