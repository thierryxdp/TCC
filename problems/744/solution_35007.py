# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "retorna a string de entrada com o símbolo # inserido no início, meio e final dela"
    a=len(s)/2
    return "#"+str(s)[:a:]+"#"+str(s)[a::]+"#"