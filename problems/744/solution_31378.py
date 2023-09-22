# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    m=len(s)//2#descobre o meio aproximado da srtring
    nova_string="#"+s[0:m]+"#"+s[m:]+"#"#cria uma nova string concatenado # entre os elementos de s
    return nova _string