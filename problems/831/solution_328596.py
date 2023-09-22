def lingua_p(palavra):
    """Função que ao receber uma palavra, retorna essa palavra na "língua
    do P", ou seja, a cada vogal na palavra, é acrescentado a letra "p"
    e a vogal original;
    str -> str"""
    linguap = ""
    i =0
    while i<len(palavra):
        if palavra[i] in "aeiouáéíóúAEIOU":
            linguap = linguap +palavra[i]+"p"+palavra[i]
        else:
            linguap = linguap+palavra[i]
        i+=1
    return linguap