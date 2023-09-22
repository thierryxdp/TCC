def repetidos(lista):
    """Dada uma lista de numeros, retorna o numero de vezes que um elemento da lista é igual ao anterior"""
    """entrada:lista
    saida: int"""
    
    pos = 0
    repeticoes = 0
    
    while pos < len(lista)-1:
        if lista[pos] == lista[pos +1]:
            repeticoes = repeticoes +1
        
        pos = pos +1
    
    return repeticoes