def primo(n):
    '''funcao que dado um numero inteiro positivo 
    retorna True se ele for primo e False se ele nao for
    int->bool'''
    resultado=0
    for elementos in range(1,n):
        if n%elementos !=0:
            resultado=resultado + 0
    return resultado==0