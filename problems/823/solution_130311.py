def faltante(lista):
    """"Retorna o numero inteiro que esta faltando.
    Parametros:
    Entrada:list
    saida:int"""
    contador=1
   	while contador<=len(lista)+1:
        if contador not in lista:
            return contador
        contador=contador+1