# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def inicio(s):
 return s[:len(s)//2]
def fim(s):
    return s[len(s)//2:]

def hashtag(s):
            return "#"+str(inicio)+"#"+str(fim)+"#"