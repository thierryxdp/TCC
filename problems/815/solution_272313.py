def insere(lista_numero,n):
    """Funcao que dada uma lista de numeros ordenada insere um numero n na posicao correta;list,int=list"""
    lista_numero=[]
    lista_numero[0:]=[n]
    lista_numero=list.sort(lista_numero)
    return lista_numero