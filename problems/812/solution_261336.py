def retira_pontuacao(frase):
    """Recebe um texto ou frase e retorna o mesmo,
mas sem pontuações e sim com espaços no lugar através
do comando replace.
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