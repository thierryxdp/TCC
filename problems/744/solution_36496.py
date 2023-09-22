# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere um caractere "#" no início,  no meio e no final dela
    str -> str"""
    Antes = s[:len(s)//2]
    Depois = s[len(s)//2:]
    s = "#" + Antes + "#" + Depois + "#"
    s  = s [: len ( s ) // 2 ] +  s [ len ( s ) // 2 :]
    return s