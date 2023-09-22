def soma_h(n):
    '''Função que retorna o valor de H com n termos, onde n é
inteiro;
	int -> float'''
    soma=0
    for elemento in range(n+1):
        soma=soma+1/elemento
    return round(soma,2)