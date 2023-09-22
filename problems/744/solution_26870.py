# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e retorna a mesma com o caractere '#' no ínicio, no meio e no fim;
    exemplo: com a entrada 'abcd' retorna '#ab#cd#';
    str => str'''
    return '#'+(s[0:int((len(s))//2)])+'#'+(s[int((len(s))//2):])+'#'