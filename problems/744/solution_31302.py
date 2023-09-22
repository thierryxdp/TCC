# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """essa função recebe uma string e insire o caractere ”#” no início, no meio e no final dela. Caso
a string apresente número par de caracteres o caractere ”#” é inserido no meio dela.
Por exemplo, se a entrada for ”abcd”, a saída é ”#ab#cd#”. Caso a string apresente número
ímpar de caracteres, o ”#” é inserido antes do meio da string. Outro exemplo: se
receber ”abcde”, a função retorna ”#ab#cde#”.
str->str"""
    tamanho= len(s)
    meio=tamanho//2

    return '#' + s[0:meio] + '#' + s[meio:] + '#'