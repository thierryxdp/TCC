# Função que irá receber uma string e inserir o caractere ”#” no ińıcio, no meio e no final dela.
# s
# str-> str
def hashtag(s):
    
    local_corte = len(s)//2
    
    return '#' + s[0:local_corte] + '#' + s[local_corte:] + '#'