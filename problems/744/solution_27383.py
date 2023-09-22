# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funçao que recebe s, insere o caractere '#' no inicio, meio e final;
    entrada: str;
    saida: str."""
     
    return  '#' + s [0: (len (s) // 2)]  + '#' + s [(len (s) // 2):]  + '#'