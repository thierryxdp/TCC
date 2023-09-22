def lingua_p(p):
    """ Função que recebe uma palavra e retorna esta mesma
    palavra na língua do P
    Entrada: str
    Saída: str """
    linguap=''
    for indice in range(len(p)):
        if p[indice] in 'aeiouéáú':
            linguap = linguap + p[indice] + 'p'+p[indice]
        else:
            linguap = linguap+p[indice]
    return linguap