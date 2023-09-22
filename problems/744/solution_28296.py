# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna uma string que recebe o caractere '#' no inicio, no meio e no fim de uma string s.
       str -> str"""
    metade_de_s = len(s)//2
    inicio_s = s[:metade_de_s]
    final_s = s[metade_de_s:]
    return str('#') + inicio_s + str('#') + final_s + str('#')