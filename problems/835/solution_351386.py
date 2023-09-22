def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        valor=min(lista)
        tupla=tupla+(valor,)
    valor=min(tupla)    
    return tupla,valor,lista