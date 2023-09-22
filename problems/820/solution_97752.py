def posLetra(frase,let,num):
    '''Função que indica a ocorrência desejada de uma letra let 
    em uma string frase. Caso exista menos ocorrências da letra do
    que a ocorrência pedida, a função retornará -1.
    frase=str,let=str,num=int->int'''
    x = str.index(frase,let,num)
    if num in frase:
    	return x
	else:
        return -1