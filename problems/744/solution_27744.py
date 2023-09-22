# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    s= s+'#'
    s= '#'+s
    
    
    lista = list(s)
    tam = len(s)

    i = int((tam/2))
  

    if tam==0:
        return  (''.join(lista)) 
    elif tam==1:
        return s
    else:
        lista [i] = '#' + lista[i]
        


    s = ''.join(lista)
    return s