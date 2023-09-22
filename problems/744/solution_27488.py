"Função que recebe uma string S e retorna hashtag entre as letras"
def hashtag(s):
    return "#"+s[:int(len(s)/2)]+"#"+s[int(len(s)/2):]+"#"