def posLetra(frase, letra_desejada, numero_da_ocorrencia):
    """recebe como entrada uma string, uma letra, e um 
    numero que indica a ocorrencia desejada da letra 
    (1 para primeira ocorrencia, 2 para segunda, etc)
    string, string, int ---> int ou string"""
    pos_atual = 0
    quant_encont = 0
	while pos_atual < len(frase) and quant_encont < numero_da_ocorrencia:
        letra_atual = frase[pos_atual]
        if letra_atual == letra_desejada:
            quant_encont = quant_encont + 1
        pos_atual = pos_atual + 1
    	if quant_encont == numero_da_ocorrencia:
        return pos_atual - 1