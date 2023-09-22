def inverte(frase):
    """Recebe um texto ou frase e utilizando a função 
retira_pontuacao retorna a mesma frase sem  letras
maiúsculas, pontuação e invertida através de separação
e junção da string.
"""
    frase_sem_ponto = retira_pontuacao(frase)
    frase_minuscula = str.lower(frase_sem_ponto)
    tira_espacos_duplos = str.replace(frase_minuscula, "  ", " ")
    frase_separada = str.split(tira_espacos_duplos, " ")
    list.reverse(frase_separada)
    frase_invertida = str.join(" ", frase_separada)
    frase_correta = str.strip(frase_invertida)
    return frase_correta