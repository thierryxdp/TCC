def filtra_pares(a,b,c,d):
    '''função que recebe uma tupla com quatro elemento e retorna uma 
    nova tupla somente com os elementos pares
    int, int, int, int -> int'''
    resto1= a%2
    resto2= b%2
    resto3= c%2
    resto4= d%2
    if resto1==0 and resto2==0 and resto3==0 and resto4==0:
        return (a,b,c,d)