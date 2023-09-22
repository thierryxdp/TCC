# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funçao que recebe s e retorna essa string no meio dela mesma;
    entrada: str;
    saida: str."""
    
    return s [0: len (s) // 2] + s + s [len (s) // 2:]