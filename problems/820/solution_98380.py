def posLetra(frase,lista,num):
    '''funçao que recebe como entrada uma string,uma letra e um numero que indica a ocorrencia desejada da letra, retorna a posiçao da string que ela se encontra: str,str,int->int'''
    listaFrase = list(frase)
    listaResp = []
    i = 0
    
    while (i<len(listaFrase)):
        if(listaFrase[i] == letra):
            listaResp.append(i)
        i += 1
    if len(listaResp) < num:
        return -1
    else:
        return listaResp[num-1]