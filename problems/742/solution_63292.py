# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Função que recebe uma string s um caractere x e o numero inteiro i e retorna a string s, exceto o elemento da posição i que é substituído por x
    :param s: str
    :param x: int
    :param i: int
    :return: str
    '''
  return str(s[0:i]) + str(x) + str(s[i + 1:])