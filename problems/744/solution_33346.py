# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
       Função que recebe uma string e returna a string 
       separada por caracteres '#' no seu ínicio, meio e
       fim, é adicionado um '#' no começo da string e 
       depois realiza a separação, tal separação é possível 
       após de dividir  quantidade (inteira) de posições 
       que a string possui pela metade e adicionar um '#' 
       e depois se adiciona a outra metade da string 
       e mais um '#'
       str -> str
    '''
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s