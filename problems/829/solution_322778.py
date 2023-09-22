def soma_h(num):
    '''Funcao que calcula e retorna o valor H com N termos onde
       N é inteiro e dado como entrada.
       : param num: int
       : return: float
    '''
    resultado=0
    for el in range(1,num+1):
        resultado=resultado+1/el
    return round(resultado,2)