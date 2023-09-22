# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    j = list(s) #Convertemos s em uma lista de chars.
    k = "#"; #Declarando uma string com a primeira '#'.
    i = 0 #Variável para cada iteração do loop.
    for l in j: #E transformamos a lista de volta em uma string.
        if i == math.floor(len(s)/2):
           k += "#"
           k += l
        else:
           k += l
        i += 1
    k += "#"
    return k #Retornamos a string final.