# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que dada uma string insere um "#" no ínicio, meio e final dela
       sendo dividida igualmente o número de caracteres para cada lado caso a
       equação tenha um número par de caracteres e com uma letra a mais para a 
       direita caso o número de caracteres seja ímpar.
       str->str
       
       Parâmetros:
       s:É a string que será aplicada a função.
       
       returns:A própria string adicionada de três "#" no início, meio e final da
       equação respectivamente. Sendo dividida igualmente o número de caracteres para cada lado caso a
       equação tenha um número par de caracteres e com uma letra a mais para a 
       direita caso o número de caracteres seja ímpar.
    """
    inicio = s[0:len(s)//2]
    restante = s[len(s)//2:len(s)]
    return "#"+inicio+"#"+restante+"#"