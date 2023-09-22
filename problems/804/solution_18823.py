def filtra_pares(elem1,elem2,elem3,elem4):
    '''recebe tupla com 4 numeros inteiros e retorna outra tupla com somente os numeros pares
    entrada: int; saida: tupla'''
    par1 = elem1 % 2
    par2 = elem2 % 2
    par3 = elem3 % 2
    par4 = elem4 % 2
    if par1 == 0 and par2 == 0 and par3 == 0 and par4 == 0:
        return (par1, par2, par3, par4)