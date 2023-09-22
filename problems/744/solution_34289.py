# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string s e adiciona um caractere # em seu início meio e fim"""
    var1 = s
    var2 = len(s)//2
    var3 = "#" + var1[0:var2]
    var4 = var1[var2:] + "#"
    return var3 + "#" + var4