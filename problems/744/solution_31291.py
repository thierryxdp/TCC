# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    var = str(s)
    return "#"var[:len(s)//2]"#"var[len(s)//2:]"#"