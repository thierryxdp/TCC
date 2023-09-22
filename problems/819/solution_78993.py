def filtro(num):
    'verifica se num é div por n'
    return num % n ==0
def filtraMultiplos(numeros,n):
    'retorna uma listas com numeros divisíveis por n'
    return list(
        filter(lambda num: num%n==0,numeros))