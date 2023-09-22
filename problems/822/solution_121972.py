def repetidos(numeros:list) -> int:
    """Função diz quantas vezes (máximo) um elemento da lista é igual ao anterior
       
       Parameters:
       numeros: lista numérica
       
       Returns:
       Maior quantidade de elementos repetidos
    """
    qtd_repeticoes = []
    i = 0
    
    while i < len(numeros):
        qtd_repeticoes += [list.count(numeros, numeros[i])]
    i = i +1
    
    return max(qtd_repeticoes)