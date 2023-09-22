# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
  
    r=int(len(s)/2)
    return "#"+s[0:r]+"#"+s[r:]+"#"