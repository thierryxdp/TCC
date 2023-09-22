def insere(lista_numero,n):
    """dada uma lista ordenada de numeros inteiros e 
    um numero inteiro n, inclui esse ultimo na posicao
    correta, ordenando a lista novamente.
    list (int,int,...) -> list (int,int,...)"""
    nova=list.append(lista_numero,n)
    nova2=list.sort(nova)
    
    return nova2