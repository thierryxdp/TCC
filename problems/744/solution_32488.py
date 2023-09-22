# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
      ''' Essa função tem como objetivo colocar 
      hashtag "#" no inicio meio e final das string'''
        return '#'+ s[0:len(s)//2]+ '#' + s[len(s)//2 + 1:len(s)] + '#'