# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
  '''função que retorne uma string com uma caractere (#)logo no início, no meio e no final dela; str -> str'''
  inicio= [:len(s)//2] final= s[len(s)//2:]
  s = "#" + inicio + "#" + final + "#" 
  s = "#" + s[:len(str1)//2] + "#" + s[len(1)//2:] + "#"
    return s