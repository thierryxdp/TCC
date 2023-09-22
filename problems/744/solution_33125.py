# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' função retorna uma string com o caractere"#" no inicio, no meio e no final dela
      str->str'''
    s ="#" + s[:len(s)//2] + "#" + s[len(s)//2:] +"#"
    return s