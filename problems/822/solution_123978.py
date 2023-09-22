def repetidos(lista:list) -> int:
    """Dada uma lista de números, a função retorna o
    número de vezes que um elemento é igual ao anterior."""
    list.sort(lista)
    i = 0
    repeticoes = 0
    
    while i < len(lista):
        ocorrencias = list.count(lista,lista[i])
        
        if ocorrencias > 1:
            repeticoes +=1
        i += ocorrencias
    
    return repeticoes