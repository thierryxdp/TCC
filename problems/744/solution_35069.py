# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    frase=s
    k=len(frase)
    w=(int(k))/2
    if k%2 ==0:
        return '#' + (frase[0:int(w)]) + '#' + (frase[int(w):]) + '#'
    else:
        j= int(w-0.5)
        return '#' + (frase[0:intj]) + '#' + (frase[int(j):]) + '#'