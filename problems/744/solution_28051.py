# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que recebe uma string e insira o caractere '#' no inicio, meio e final da string;
    string,strin,string -> string'''
    n = (len(s)//2)
    return '#'+s[0:n]+'#'+s[n:]+'#'