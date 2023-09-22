def filtra_pares(n):
    """ iresmos abrir uma tupla para colocar suas condições
    depois iremos analisar cada termo dessa tupla e dividir por 2 que assim 
    sabermos se é par ou não"""
    npares=()
    if n[0]%2 == 0:
       
        npares+=(n[0],)
        
    if n[1]%2 == 0:
        
        npares+=(numeros[1],)
    if n[2]%2 == 0:
        npares+=(n[2],)
    if n[3]%2 == 0:
        npares+=(n[3],)
    return npares