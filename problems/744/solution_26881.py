# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ função que receba uma string e insira o caractere "#" mp início, no meio e no final dela;
    string-> string"""
    var1= (len(s)//2)
    return "#"+s[0:len(s)]"#"s[len(s):]+ "#"