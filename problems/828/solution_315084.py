def qtd_divisores(num):
    '''recebe um numero como entrada e retorna quantos
    divisores esse numero possui
    int->int'''
    lista=list(range(1,num+1))
    divisores=[]
    for elemento in lista:
        if num%elemento==0:
            divisores=divisores+[elemento]
    return len(divisores)

def primo(num):
    '''retorna true se o numero for impar e false se ele
    nao for
    int->bool'''
    x= qtd_divisores(num)
    return x<=2