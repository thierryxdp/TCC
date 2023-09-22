def repetidos(numeros:list) -> int:
    """Função diz quantas vezes (máximo) um elemento da lista é igual ao anterior
       
       Parameters:
       numeros: lista numérica
       
       Returns:
       Maior quantidade de elementos repetidos
    """
    qtd_repeticoes = 0
    i = 1
    
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            qtd_repeticoes += 1
        i = i +1
    return qtd_repeticoes