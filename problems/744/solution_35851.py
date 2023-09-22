# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada uma string como parâmetro retorna amesma string com # no inicio, meio e final dela.'''
    quociente= len(s)/2
    resto= len(s)%2
    if (quociente == 0):
        return '##'
    elif(resto == 0):
        firstHalf= s[0:quociente+1] 
        secHalf= s[quociente+1:]
        return '#'+ firstHalf +'#'+ secHalf
    elif(resto>0):
        firstHalf= s[0:quociente+1] 
        #i
        secHalf= s[quociente+1:]
        #i
        return '#'+ firstHalf +'#'+ secHalf