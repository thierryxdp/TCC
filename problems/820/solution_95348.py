def posLetra(string, letra, n):
    '''funcao que dados uma string, uma letra e um numero, retorna a posicao da ocorrencia desejada da letra
       caso exista menos ocorrencias da letra do que a ocorrencia pedida, retorna -1
       string, string, int -> int '''
    contaocorren = 0
    posicao = 0
    if(str.find(string, letra) == -1):
        return -1
    else:
    	while(contaocorren < n):
            if(str.find(string, letra, posicao)>=0):
    	    	contaocorren += 1
            	posicao = str.find(string, letra, posicao)
            
    	return posicao