def soma_h(n):
    '''Função que soma todos os valores da divisão de por numeros até N dado como parâmetro
    	int -> int'''

    listadesoma = []
    
    for h in range(1,n+1):

        listadesoma+=[1/h]

    return sum(listadesoma)