def soma_h(numero):
    '''funçao que calcula e retorna o valor H com N termos,
onde N é inteiro e é dado como entrada.
int -> float'''
    h=0
    for c in range(numero):
        h+=1/(c+1)
    return round(h,2)