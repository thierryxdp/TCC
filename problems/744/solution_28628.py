# Função que recebe uma string e insira o caráctere "#" no início, meio e no final dela.
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pos = len(s)//2
    return "#"+s[:pos]+"#"+s[pos:]+"#"