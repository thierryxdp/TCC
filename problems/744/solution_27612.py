# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere o caractere # no inicio, meio
       e fim da string
       
       Parameters:
       s: String escolhida
       """
    return str('#') + s[0:len(s)//2] + str('#') + s[len(s)//2:] + str('#')