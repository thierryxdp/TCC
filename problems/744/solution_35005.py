# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "retorna a string de entrada com o símbolo # inserido no início, meio e final dela"
    return "#"+str(s)[:(len(s)/2):]+"#"+str(s)[len(s)/2::]+"#"