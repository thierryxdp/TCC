def par(x):
    '''Verifica se um numero inteiro e par.
    #parametros | in: int -> out: bool (True p/ par, False p/ impar)'''
    if type(x)==int:
        if x%2==0:
            return True
        else:
            return False
    else:
        return 'Digite um numero inteiro.'
def filtra_pares(*lista):
    '''Digite quatro numeros inteiros. Retorna os numeros pares na
    ordem digitada.
    #parametros | in: tupla(int, int, int, int (numeros da lista)) ->
    out: tupla (somente com os numeros pares)'''
    [[a,b,c,d]]=lista
    if type(lista[0][0])==int and type(lista[0][1])==int and type(lista[0][2])==int and type(lista[0][3])==int: #dentro dos types estao os indices da lista
        return filter(par,lista[0])
    else:
        return 'Digite somente numeros inteiros.'