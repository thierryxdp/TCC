def faltante(lista):
    """Funcao que, dado uma lista de entrada de quais pecas Joaozinho tem,
    retorna um numero inteiro correspondente a peca que esta faltando;
    lista -> int"""
    contador=0
    while contador< len(lista)+1:
        if len(lista)+1-contador not in lista:
            return len(lista)-contador
        contador+=1