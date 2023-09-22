# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string_2): 
    g=len(string_2)
    if (g%2==0):
        j=g//2
        return str("#"+string_2[:j]+"#"+string_2[j:]+"#")
    else:
        j=g//2
        return str("#"+string_2[:j]+"#"+string_2[j:]+"#")