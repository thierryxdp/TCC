def filtraMultiplos(lista, div):
    """ dada uma lista de entrada contendo uma quantidade sortida de numeros aleatorias
e um numero, este ultimo sera o divisor e tera como retorno da funcao uma lista
com os numeros que sao divisiveis por ele. ([list],int) -> [list]
ex filtraMultilpos([2,3,4,5],3) = [3]"""
    
    multiplos = []
    i = 0
    while i<len(lista):
        if lista[i]%div==0:
            multiplos = multiplos + [lista[i],]
        i = i+1
    return multiplos