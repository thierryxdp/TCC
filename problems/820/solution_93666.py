def posLetra(string,letra,numero):
    """Retorna em que posicao da string a ocorrencia da letra esta.Caso exista menos ocorrencias da letra do que a ocorrencia pedida,retorna-1.str,str,int-->int"""
    s=string
    z=1
    if str.count(s,letra)<numero:
        return -1
	while z!=numero:
        string=str.replace(string,letra,' ',1)
        z=z+1
        return str.index(string,letra)