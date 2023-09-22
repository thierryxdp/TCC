# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

palavra= ""
def hashtag(palavra):
    a=len(palavra)
    b= a//2
    return "#"+palavra[:b]+"#"+palavra[b:]