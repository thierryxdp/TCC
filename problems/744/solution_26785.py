# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string recebida com o caractere '#' no início, meio e fim da string;
    string -> string"""
    if len(s)%2 == 0:
        fatia1 = s[:len(s)//2]
        fatia2 = s[len(s)//2:]
        return '#'+fatia1+'#'+fatia2+'#'
    else:
        fatia1 = s[:len(s)//2]
        fatia2 = s[len(s)//2:]
        return '#'+fatia1+'#'+fatia2+'#'