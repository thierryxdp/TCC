def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        valor=min(lista)
        tupla=tupla+(valor,)
    for lista in matriz:
        valor1=min(tupla)    
    return tupla,valor