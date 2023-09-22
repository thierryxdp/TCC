# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string s e insere "#" no inínio, no 
    meio e no final dela"""
    return "#"+str(s)[0:len(s)//2]+"#"+str(s)[len(s)//2:]+"#"