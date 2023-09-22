def filtra_pares(numeros):
    '''retorna apenas os numeros pares dados nas entradas
    entradas:tupla com int,int,int,int
    saida:tupla vazia ou tupla com 1 a 4 int'''
    if (numeros)[0:]%2==0 and (numeros)[1:2]%2!=0 and (numeros)[2:3]%2!=0 and (numeros)[3:]%2!=0:
        return (numeros[0:],)