# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string_2): 
    g=len(string_2)
    if (g%2==0):
        j=(g//2)+1
        return print("#"+string_2[:j]+"#"+string_2[j:]+"#")
    else:
        j=g//2
        return print("#"+string_2[:j]+"#"+string_2[j:]+"#")