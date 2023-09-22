def faltante (lista):
    "Função que dada uma lista numerada de 1 a N, retornar qual o numero inteiro está faltando neste intervalo; list ->int"
    indice = 1
    lista.sort()
    while lista [ indice - 1] == indice:
        indice += 1 
        if indice > len(lista):
            return indice 
    return indice