def lingua_p(palavra):
    """Dada uma palavra a função traduz para a língua do P
    e a retorna.
    Parametros de Entrada: str
    Retorna: str"""

    i=0
    
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            palavra= palavra[:i+1]+'p'+palavra[i+1:]
            i=i+2
        else:
            i=i+1
    palavra= palavra.lower()
    return palavra