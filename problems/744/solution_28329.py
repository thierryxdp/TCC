# Função que insere o caractere "x"no início meio e final dada string s 
# str-> str
def hashtag(s):
    s="#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return s