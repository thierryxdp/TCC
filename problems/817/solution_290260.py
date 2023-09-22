def acima_da_media (notas):
    """Função retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list"""
    
    media = sum(notas) / len (notas)
    notas_acima = []
    
    for maiores in notas:
        if miores > media:
            notas_acima.append(maiores)
            
    return media, list.sort(notas_acima)