# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
  
"""
Utiliza-se a função len para que se consiga chegar à metade da string s
,assim somando a hashtag antes da string começar com sua len sobre 2
(metade da palavra, com duas barras para se chegar a um inteiro), assim 
como o retorno no len sobre 2 até o final da string s,com a soma da
string de um hashtag também no meio e no final da palavra
"""

    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"