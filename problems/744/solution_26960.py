# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Recebe um string s e adiciona o caractere "#" no início, meio e fim da strinh s, string -> stting """;
    s = "#"+ s[:len(s) // 2] + "#" + s[len(s) // 2:] + "#"
    return s;