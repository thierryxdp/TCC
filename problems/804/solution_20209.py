def par(x):
    """Define se um número é par"""
    """int/float->bol"""
    return num%2==0
def filtra_par(lista):
    """Função que recebe 4 números e filtra somente os números pares"""
    if not par(lista[0]):
        lista[0]=