def acima_da_media (notas):
    """Função que, dada uma lista com notas, retorna uma lista ordenada com notas que ficaram acima da media
    Entrada: lista[int]
    Saída: lista[int]"""
    
    media = sum(notas) / len(notas)
    list.sor(notas)
    return