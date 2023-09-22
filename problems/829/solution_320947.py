def soma_h(n):
    """Retorna um valor da variável H, conforme o número n 
       recebido como entrada
       parâmetro de entrada:int
       parâmetro de saída:float"""
    H=0
    for n in renge(1,n+1):
        H=H+1/n
    return round(H,2)