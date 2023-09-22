# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Insere # no inicio, meio, fim de uma string
    onde a string de entrada len(s) > 3
    string -> string """
    " Pega a parte inteira da meteda da string "
    i = len(s)//2
    nova = "#"+[:i]+"#"+[i:]+"#"
    return nova