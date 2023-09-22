# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """dada uma palavra, calcula a quantidade de caracteres e insere (#) no início, no meio e no fim da palvra
    exemplo: abcd-> #ab#cd#
    entrada: str
    retorna: str"""
    num_carac= len(s)
    metade_carac= num_carac//2
    inicio_palavra= s[0:metade_carac]
    final_palavra= s[metade_carac:]
    return '#'+ inicio_palavra +'#'+ final_palavra+'#'