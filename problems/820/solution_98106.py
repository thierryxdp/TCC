def posLetra(frase, letra, ocorrencia):
    """Função que dada uma frase, uma letra da frase e qual a ocorrência
    dela, por exemplo: 2 para a segunda ocorrência, retorna o indice da
    string dessa ocorrência, caso exista menos ocorrências do que o número
    dado, retorna -1;
    str, str, int -> int"""
    indice = 0 
    index = frase.find(letra)
    if index < ocorrencia: 
        while indice < len(frase):
            index = frase.find(letra)
            indice += 1
        return index 
    else:
        return -1