def insere(lista_numero, n):
    """Função que inclui um numero inteiro (n) na sua posição
    correta.
    list, int -> list"""
    
    lista_numero.insert (0, n)
    lista_atualizada = sorted(lista_numero)
    
    return lista_atualizada