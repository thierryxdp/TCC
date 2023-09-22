# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que recebe uma string e retorna a mesma porem com # no inicio meio e fim;
    string = string'''
    x = "#"
    y = len(s)//2
    
    return x + s[:y] + x + s[y+1:len(s)] + x