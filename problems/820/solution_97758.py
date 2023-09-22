def posLetra(frase,let,num):
    '''Função que indica a ocorrência desejada de uma letra let 
    em uma string frase. Caso exista menos ocorrências da letra do
    que a ocorrência pedida, a função retornará -1.
    frase=str,let=str,num=int->int'''
    z=str.count(let,frase)
    if z < num:
        y=-1
    	return y
    else:
        x = str.index(frase,let,num)
        return x