def repetidos(lista):
    '''
    	Função que recebe como parâmetro 
        de entrada uma lista de números
        e retorna o número de vezes que 
        um elemento da lista é igual ao
        elemento anterior
        : param lista: list
        : return: int
    '''
    contador = 0
    indice = 0
    
    while indice+1 < len(lista):
        if lista[indice] == lista[indice+1]:
            contador+=1
        indice+=1
    
    return contador