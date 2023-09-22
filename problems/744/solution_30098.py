# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string s e retorna a mesma string s acrescida da
string "#" no começo, no final e no meio da string s;
Entrada: string ; Retorno: string'''
    meio= (len(s))//2
    return '#'+ s[:meio] + "#" + s[meio:] + "#"