# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string "s", um caractere "x" e um número inteiro "i" 
    e substitui o caractere de indice i da string s pelo caractere x informado
    assinatura - string, int, int -> string
    testes:
    substitui("victor","x",5) == 'victox'
    substitui("programação","i",4) == 'progiamação'
    """
    string_alterada1 = s[:i] + str(x) + s[i+1:]
    if i<0 or i>len(s):
        return "índice invalido"
    else:
        return string_alterada1