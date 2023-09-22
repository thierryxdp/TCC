def uppCons(texto):
    """frase que retorna a frase com todas as consoantes
    em maiusculas"""
    passador = 0
    fraseFinal = ''
    while passador < len(texto):
        if texto[passador] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕÂâ':
            fraseFinal += texto[passador].upper()
        else:
        	fraseFinal += texto[passador]
        passador += 1
    return fraseFinal