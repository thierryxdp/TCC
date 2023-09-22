def insere(lista_numero,n):
    """função que inclui n na posição correta da lista de forma que a mesma continue crescente
    através dos dados de entrada 'lista_numero' e 'n';
    Entrada: list, int
    Saída: list"""
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero