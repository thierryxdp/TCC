# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #Essa função recebe uma string e insere o caractere hashtag no inicio, no meio e no final da string
    antes = s[:len(s)//2]
    depois= s[len(s)//2:]
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s