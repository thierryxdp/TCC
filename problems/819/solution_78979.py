def filtro(num, n):
    'Verifica se num é divisivel por n'
    return num%n == 0

def filtraMultiplos(numeros, n):
    'Filtra da lista numeros os divisiveis por n'    
    
    return list(
        filter(filtro, numeros, [n]*len(numeros))
	    )