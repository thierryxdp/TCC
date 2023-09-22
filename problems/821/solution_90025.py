def fatorial(numero):
    """Função que calcula e retorna o fatorial de um número"""
    """Parâmetro de entrada: int"""
    """Parâmetro de saída: int"""
    resultado=1
    count=1
    while numero>=count:
        resultado*=count
        count+=1
    print (resultado)