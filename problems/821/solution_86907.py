def fatorial(numero):
    '''dado um numero, retorna a multiplicação dele por ele menos um, sucessivamente até 1
    entrada:int
    saida:int'''
    if numero == 0 or numero == 1:
        return 1 
    else:
        return numero * fatorial(numero-1)