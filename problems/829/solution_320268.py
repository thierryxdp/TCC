def soma_h(n):
    '''Função que calcula e retorna o valor de h com n termos, onde n é o inteiro dado como parametro de entrada; int->int'''
    l1=[]
    soma=0
    lista= list(range(n))
    for c in lista:
        list.append(l1, 1/(c+1))
        soma=soma+l1[c]
    return round(soma,2)