def insere(lista_numero,n):
    """Função que dada uma lista ordenada(crescente) incluindo uma numero n na posição correta.
    parametros: lista,int->lista"""
    return list.sort(lista_numero + [n])