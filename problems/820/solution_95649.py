def posLetra (frase, letra_desejada, numero_da_ocorrencia):
    """recebe como entrada uma string, uma letra, e um 
    numero que indica a ocorrencia desejada da letra 
    (1 para primeira ocorrencia, 2 para segunda, etc)
    str,str,int->int"""
    posicao_atual = 0
    quantidade_encontrada = 0
    
    while posicao_atual < len(frase) and quantidade_encontrada < numero_da_ocorrencia:
        letra_atual = frase[posicao_atual]
        if letra_atual == letra_desejada:
            quantidade_encontrada += 1
        posicao_atual += 1
        
    if quantidade_encontrada == numero_da_ocorrencia:
        return posicao_atual-1