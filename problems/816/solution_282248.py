def maiores(lista,n):
    """Dados uma lista e um número inteiro, a função analisa a lista e se tiver algum numero manior que o n dado 
    nos parametros, ela insere esse numeros em uma nova lista e na saida ela devolve essa lista nova ordenada. Caso não
    tenha nenhum número maior que o n, ela devolve uma lista vazia"""
    maior=[]
    for item in lista:
        if item >n:
            maior.append(item)
    maior.sort()
    return maior