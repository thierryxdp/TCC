# Ao inserir uma string adiciona uma hashtag no início, meio e fim da string.
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:len(s)] + '#'