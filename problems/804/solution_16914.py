def filtra_pares(tupla):
    '''função que recebe uma tupla com quatro elementos inteiros e retorna uma tupla com apenas os elementos pares.
    entrada:tupla
    saída:tupla'''
    if (tupla[0])%2==0 or (tupla[1])%2==0 or (tupla[2])%2==0 or (tupla[3])%2==0 :
        return (tupla[0],tupla[1], tupla[2], tupla[3])