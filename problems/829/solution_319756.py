def soma_h(n):
    '''Função que recebe como entrada um número(n) e retorna o valor da função H com os n termos.
       parâmetro de entrada:int
       valor de retorno:float'''
    trecho=list(range(1,(n+1)))
    h=[]
    for i in trecho:
        result=(1/i)
        h=h+[result]
    return round((sum(h)),2)