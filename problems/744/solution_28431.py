# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(texto):
    comeco = len(texto)//2
    final = -len(texto)//2
    return '#' + texto[:comeco]+'#'+texto[final'