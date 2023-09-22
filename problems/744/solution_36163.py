# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n=list(s)
    ''' comecei convertendo a string s em uma lista com os caracteres'''
    a=len(n)
    ''' criei essa variavel com os tamanho da lista, ou seja, o tamanho da string'''
    b=(a//2)
    ''' com a variavel anterior eu criei essa que vai me retornar a posição do meio'''
    list.insert(n,a,"#")
    ''' aqui a ordem era importante, então coloquei o 1° # no final, pois isso não muda o meio inteiro da palavra
    nem a posição do caractere inicial'''
    list.insert(n,b,"#")
    ''' agora coloquei o caractere # no meio, e é importante colocar esse por segundo pois caso contrário
    não obtenho o resultado desejado'''
    list.insert(n,0,"#")
    ''' por fim o primeiro #, que deve ser o último, pois se for adicionado antes dos outros, ele acaba mudando a posição de onde os
    # precisam ser colocados, assim, não obtendo o resultado desejado.'''
    strn = ''.join(n)
    ''' converti a lista em string'''
    return strn ''' retornei o resultado: String --> String'''