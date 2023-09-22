# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
 '''Função que põe a string '#' no ínicio,meio e fim na string de entrada; string-->string'''

 meio= len(s)//2
 string_1= s[:meio]
 string_2= s[meio:]

 return '#'+string_1+'#'+string_2+'#'