def qtd_divisores(numero):
    '''recebe um numero como entrada e retorna quantos
    divisores esse numero possui
    int->int'''
    lista=list(range(1,numero+1))
    divisores=[]
    for elemento in lista:
        if numero%elemento==0:
            divisores=divisores+[elemento]
    return len(divisores)

def primo(numero):
    '''retorna true se o numero for impar e false se ele
    nao for
    int->bool'''
    x= qtd_divisores(numero)
    return x<=2