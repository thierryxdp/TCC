def faltante(lista):
    """
    Essa função recebe uma lista com as peças numeradas de um 
    quebra-cabeça e retorna qual peça está faltando;
    list -> int
    """
    str1 = ''
    for x in lista:
        str1 += str(x)
    for i in range(1, len(str1) + 1):
        if not str(i) in str1:
            return i