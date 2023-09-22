# Função que recebe uma string e insira um caractere "#" no início, no meio e no final dela
# str-> str
def hashtag(s):
    return '#'+ hashtag[0] + '#' + hashtag[(len(hashtag)-1)/2] + '#' + hashtag[(len(hashtag)-1)]