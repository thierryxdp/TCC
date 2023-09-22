def posLetra (string,letra,n):
    '''função que recebe como entrada uma str,uma letra e um 
    número. Essa função retorna em que ocorrencia(N) da str a
    letra está;str->int'''
    resposta=[]
    resposta2=''
    rodada=0
    while str.count(string,letra)>n:
        if letra in string:
            resposta=(str.find(string,letra,0,(len(string))))
        elif str.count(string,letra)<n:  
            resposta=-1
        
        rodada+=1
    return resposta