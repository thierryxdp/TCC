def retira_pontuacao(frase):
    """Recebe um texto ou frase e retorna o mesmo,
mas sem pontuações e sim com espaços no lugar.
str -> str
"""
    string = frase
    troca_tra = str.replace(string, "-", " ")
    troca_vir = str.replace(troca_tra, ",", " ")
    troca_2po = str.replace(troca_vir, ":", " ")
    troca_pov = str.replace(troca_2po, ";", " ")
    troca_int = str.replace(troca_pov, "?", " ")
    troca_exc = str.replace(troca_int, "!", " ")
    troca_ret = str.replace(troca_exc, "...", " ")
    troca_pon = str.replace(troca_ret, ".", " ")
    return troca_pon
def inverte(frase):
	"""Recebe um texto ou frase e utilizando a função 
retira_pontuacao retorna a mesma frase sem  letras
maiúsculas, pontuação e invertida.
"""
    frase_sem_ponto = retira_pontuacao(frase)
    frase_minuscula = str.lower(frase_sem_ponto)
    tira_espacos_duplos = str.replace(frase_minuscula, "  ", " ")
    frase_separada = str.split(tira_espacos_duplos, " ")
    list.reverse(frase_separada)
    frase_invertida = str.join(" ", frase_separada)
    frase_correta = str.strip(frase_invertida)
    return frase_correta