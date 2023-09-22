def posLetra(frase,letra,num):
    """retorna a posicao da string em que a letra esta, caso exista menos ocorrencias da letra do que a ocorrencia pedida, a funcao retornar -1."""
	pos=-1
    if letra not in frase or num>frase.count(1) :
        return pos
    else:
    	while num!=0:
    		num=num-1
    		pos=str.find(frase,letra,pos+1)
        return pos