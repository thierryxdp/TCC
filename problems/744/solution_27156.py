# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ função que insere uma hashtag (#) no início, no meio e ao fim de um string 
    string -> string """
    return '#' + s[0: int(len(s)/2)] + '#' + s[int(len(s)/2) :] + '#'