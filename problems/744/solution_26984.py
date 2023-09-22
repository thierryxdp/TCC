# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """dada uma string s, a função retorna a mesma string, 
porém com o caractere "#" no seu início, meio e fim. Por
exemplo, dado "1234", a função retorna"#12#34#"
string-->string"""
    return "#"+s[0:(len(s)//2)+1)]+"#"+s[(len(s)//2)+1:len(s)]+"#"