# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(sabor):
    meio=int(len(sabor)/2)
    return "#"+sabor[:meio]+"#"+sabor[meio:]+"#"