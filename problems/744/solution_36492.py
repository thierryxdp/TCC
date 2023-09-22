# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere um caractere "#" no início,  no meio e no final dela
    str -> str"""
    Antes = s[:len(str1)//2]
    Depois = s[len(str1)//2:]
    s = "#" + antes + "#" + Depois + "#"
    s  =  "#"  +  s [: len ( str1 ) // 2 ] +  "#"  +  s [ len ( str1 ) // 2 :] +  "#"
    return s