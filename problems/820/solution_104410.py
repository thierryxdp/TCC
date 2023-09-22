def posLetra (frase, L, n):
    """ Dado uma string, uma ltra e o número da ocorrencia da letra passada, retorna a rosição da string para aquela ocorrenciaa.
    entrada string, string, inteiro -> saida inteiro. """
    
    i = 0 
    ocorrencia = 0 
    while i < len(frase) and ocorrencia < n:
        if frase[i] == L:
 			ocorrencia = ocorrencia + 1
        i = i + 1
        return i