def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        valor=min(lista)
        tupla=tupla+(valor,)
    valor1=min(tupla)    
    return valor