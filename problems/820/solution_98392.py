def posLetra(frase,letra,numero):
    """Função que recebe uma string, uma letra, e um numero e retorna a 
    posição da string que a ocorrencia está, str,bool,int-->str"""
    LisFrase=list(frase)
    LisResp=[]
    i=0
    while (i<len(LisFrase)):
        if (LisFrase[i]==letra):
             LisResp.append(i)
        i+=1
    if len(LisResp)<numero:
        return -1
    else:
        return LisResp[numero-1]