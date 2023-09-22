# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe como parâmetro uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string e retorna a string s com o elemento da posição i substituído pelo caractere x;
	assinatura: str, str, int --> str
    Casos de teste:
    substitui('pato', 'a', 3) == 'pata'
    substitui('branco', 'a', 5) == 'branca'
    substitui('meia', 'o', 3) == 'meio
    '''
    if i >= 0 and i <= len(s):
        s = s.replace(s[i], x)
        return s