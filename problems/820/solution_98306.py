#Questão 3
def posLetra(frase, letra, ocorrencia):
    """Função que dada uma frase, uma letra da frase e qual a ocorrência
    dela, por exemplo: 2 para a segunda ocorrência, retorna o indice da
    string dessa ocorrência, caso exista menos ocorrências do que o número
    dado, retorna -1;
    str, str, int -> int"""
    indice = 0 
    letras =[]
    quantidade = str.count(frase, letra)
    if quantidade < ocorrencia:
        letras = -1
        return letras
    else:
        while indice < len(frase):
            if frase[indice] = letras:
                letras += [str.find(frase, letras, indice)]
            indice += 1
    novaOcorrencia = letras[ocorrencia -1]
    return novaOcorrencia