"""
Nesta função, a ideia foi criar 2 variáveis para serem o começo e o fim da
str, assim adicionando os '#' entre as 2 partes da palavra, com isso o inicio
ficou caracterizado como cáctere 0 até tamanho da palavra//2 até, usando o 
tamanho da palavra//2 para divídi-la ao meio. E depois o final ficou como 
o tamanho da palavra//2 até o tamanho total da palavra. Bem direto e simples.
str-> str
"""
def hashtag(s):
    x = len(s)
    inicio = s[0:x//2]
    fim = s[(x//2):x]
    return str('#')+inicio+str('#')+fim+str('#')