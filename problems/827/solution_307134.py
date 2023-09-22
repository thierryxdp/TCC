def lista(num):
    '''retorna uma lista de 1 ate o numero
    int->list'''
    x=num+1
    return list(range(1,x))
    
def qtd_divisores(num):
    '''recebe um numero como entrada e retorna quantos
    divisores esse numero possui
    int->int'''
    lista1=lista(num)
    divisores=[]
    for elemento in lista1:
        if num//elemento==0:
            divisores=divisores+[elemento]
    return len(divisores)