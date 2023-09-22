# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #entrar com string
    string = "#"+s+"#"  # concatenação
    meio = len(s) //2 # leitura do tamanho p poder fatiar
    return string[:meio] + "#" + string[meio:] #fatiamento