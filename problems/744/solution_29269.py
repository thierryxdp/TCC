# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna uma string com '#' no meio
    str-->str'''
    numeros= len(s)//2
   return"#"+s[:numeros]+"#"+s[numeros-1:]"#"