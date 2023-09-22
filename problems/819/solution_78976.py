def filtro(num,n):
    'verifica se num é div por n'
    return num % n ==0
def filtraMultiplos(numeros,n):
    'retorna uma listas com numeros divisíveis por n'
    return filter list(filtro,numeros)