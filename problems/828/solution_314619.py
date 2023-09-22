def primo(n):
    '''funcao que dado um numero inteiro positivo 
    retorna True se ele for primo e False se ele nao for
    int->bool'''
    eh_primo= True
    nao_eh_primo= False
    for elementos in range(1,n):
        if n%elementos !=0:
            resultado=eh_primo
        if n%elementos==0:
            resultado= nao_eh_primo
    return resultado