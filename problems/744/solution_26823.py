# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "a função calcula a hasthag que receba uma string e insira o caractere # no inicio, no meio e no final dela str-> str"
    string1 = s[0:len(s)//2]
    string2 = s[len(s)//2:]
    return "#"+string1+"#"+string2+"#"