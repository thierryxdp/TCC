def insere(lista_numero,n):
    """Função que dada um lista em ordem crescente e um número, é retornado a lista com o número na posição certa 
       Parâmetros: list,int -> list"""
    lista_numero.insert(0,n)
    nova = list.sort(lista_numero)
    return nova