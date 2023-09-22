# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """essa função, dada uma string qualquer, ira retornar a mesma
    string dada adicionando o caractere # no inicio no meio e no final da string.
    str->str
    """
   
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s