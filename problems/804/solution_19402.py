def filtra_pares(tupla_inteiros): #da um nome decente pras variaveis homi
    """funcao que, dada uma tupla com 4 numeros inteiros, retorna uma tupla
    contendo apenas os numeros pares dela; tuple -> tuple"""

   def filtra_pares(tupla_inteiros): #da um nome decente pras variaveis homi
    """funcao que, dada uma tupla com 4 numeros inteiros, retorna uma tupla
    contendo apenas os numeros pares dela; tuple -> tuple"""
  
   lista_pares = []
    
    if tupla_inteiros[0] % 2 == 0:
        lista_pares = lista_pares.append(tupla_inteiros[0])
    if tupla_inteiros[1] % 2 == 0:
        lista_pares = lista_pares.append(tupla_inteiros[1])
    if tupla_inteiros[2] % 2 == 0:
        lista_pares = lista_pares.append(tupla_inteiros[2])
    if tupla_inteiros[3] % 2 == 0:
        lista_pares = lista_pares.append(tupla_inteiros[3])

    tupla_pares = tuple(lista_pares)

    return tupla_pares