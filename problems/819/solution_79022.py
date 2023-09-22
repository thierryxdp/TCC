def filtro(num):
    'Verifica se num é divisivel por n'
   
    return num%n == 0

def filtraMultiplos(lista,n):
    'Filtra da lista numeros os divisiveis por n'
    
    return list(filter(lambda num: num%n == 0, numeros))