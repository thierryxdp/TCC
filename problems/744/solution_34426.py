# Coloque um comentário dizendo o que a função faz
# aux = contagem de caracteres, a = recebe o inteiro da divisao de aux, 
# aux2 e aux3 dividem a string
# str-> str
def hashtag(s):
    aux=len(s)
    a= int (aux/2)
    aux2 = s[0:a]
    aux3 = s[a:aux]
    if aux==1:
        return '##'+str(s)+'#'
    else:
    	return '#'+str(aux2)+'#'+str(aux3)+'#'