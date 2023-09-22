def soma_h(n):
    '''Função que calcula e retornar o valor H( que é o número 1 somando com frações de ½ até o denominador atingir o número n  ) assim com N termos, onde N é inteiro e  dado como entrada.
     int->flot'''
    soma=0
    for i in range(1,n+1):
        soma+=1/i
    return round(soma,2)