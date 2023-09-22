def posLetra(string,letra,num):
    """retorna a posicao da string em que a letra esta, caso exista menos ocorrencias da letra do que a ocorrencia pedida, a funcao retornar -1."""
	pos=-1
    
    while num!=0 and letra in string or num<=str.count(string, letra):
    		num=num-1
    		pos=str.find(string,letra,pos+1)
    return pos