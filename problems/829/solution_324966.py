def soma_h(n):
    '''Função calcula a soma de n termos: 1/1+1/2+1/3+...+1/n
       int --> float'''
    lista=list(range(1,n+1))
    soma=[]
    for i in lista:
        soma.append(1/i)
    return round(sum(soma),2)