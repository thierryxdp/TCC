# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que dada uma string, retorna a própria
    string com o caractere "#" no início, no meio e no final
    entrada: str
    saída: str"""
    
    return '#'+s[:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'