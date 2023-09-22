# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    '''função que recebe uma string e insere o caractere "#" no inicio, no meio e no final'''
    '''str -> str'''
      meio = len(string)//2
      return "#" + string[:meio]+"#"+ string[meio:]+ "#"