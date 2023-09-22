def posLetra (string,letra,n):
    '''função que recebe como entrada uma str,uma letra e um 
    número. Essa função retorna em que ocorrencia(N) da str a
    letra está;str->int'''
    resposta=[]
    resposta2=''
    rodada=0
    while rodada<len(string):
        if str.count(string,letra)>=n:
            resposta=(str.find(string,letra,0,(len(string))))
        if str.count(string,letra)<n:
            resposta=-1
        rodada+=1
    return resposta