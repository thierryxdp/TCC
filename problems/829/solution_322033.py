def divisao_h(n:int)->float:
    '''Divide o valor n recebido por 1'''
    return 1/n
def soma_h(n:int)-> int:
    '''Soma a divisão de 1 por 'n' termos'''
    k=sum(list(map( div_h, range(n,0,-1))))
    return round(k,2)