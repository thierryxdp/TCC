def qtd_divisores(n):
    ''' Função que retorna quantos divisores o n possui.
        int---->int'''
    x = 0
    resultado = 0
    while x<n:
        x+=1
        if n%x==0:
            resultado+=1
    return resultado