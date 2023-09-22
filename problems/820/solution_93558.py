def posLetra(string,letra,numero):
    """Retorna em que posicao da string a ocorrencia da letra esta.Caso exista menos ocorrencias da letra do que a ocorrencia pedida,retorna-1.str,str,int-->int"""
    s=string
    str.replace(s,letra," ",numero-1)
    if str.index(string,letra)==0:
        return -1
    else:
        return str.index(string,letra)