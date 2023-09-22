def primo(numero):
    '''Funcao que pega o numero de entrada e retorna se ele é primo ou não. 
    	int,int→bool'''
    tamanho= numero+1
    lista=[]
    for divisor in range(1,tamanho):
        if numero%divisor==0:
            lista.append(divisor)
    if len(lista) > 2:
        return False
    else:
        return True