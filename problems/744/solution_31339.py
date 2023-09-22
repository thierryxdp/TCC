# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=list(s)
        s.insert(0,"#")
        s.insert(len(s),"#")
        s.insert(len(s)/2,"#")
        s=''.join(s)
        return s