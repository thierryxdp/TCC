def filtra_pares(n):
    """ iresmos abrir uma tupla para colocar suas condições
    depois iremos analisar cada termo dessa tupla e dividir por 2 que assim 
    sabermos se é par ou não"""
    n=()
    if numeros[0]%2 == 0:
       
        n+=(numeros[0],)
        
    if numeros[1]%2 == 0:
        
        numeros_pares+=(numeros[1],)
    if numeros[2]%2 == 0:
        numeros_pares+=(numeros[2],)
    if numeros[3]%2 == 0:
        numeros_pares+=(numeros[3],)
    return numeros_pares