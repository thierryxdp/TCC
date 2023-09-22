# Funcao que recebe uma string e insere o caractere"#" no inicio, meio e fim
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"