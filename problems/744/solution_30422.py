# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dado a frase(s)=str, retorna a frase com #, no inicio, no meio e no final'''
    frase=s
   x=int(len(s)/2)
   return '#'+frase[:x]+'#'+frase[x:]+'#'