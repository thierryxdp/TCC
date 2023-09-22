#Exercíco_04:
''' Essa função recebe uma lista de números e retorna a quantidade de vezes em que os termos se repetem 
    quando estão na juntos. '''
''' list ---> int. '''

def repetidos(list_n):
    i=0
    s=0
    while i < len(list_n)-1:
        x = list_n[i]
        y = list_n[i+1]
        if x == y:
            s += 1
        else:
            s += 0 
        i += 1
    return s