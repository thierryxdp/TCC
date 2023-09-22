def hashtag(s):
# Função que recebe um string e insere o caracter "#" no 
# início, no meio e no final dela.
# str-> str
def hashtag(s):
    X=s
    t=len(X)
    return "#"+X[0:(t//2)]+"#"+X[(t//2):]+"#"