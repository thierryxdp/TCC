def maiores(l, n):
    """Dada uma lista l e um inteiro n, a função acima retorna os inteiros de l maiores que n.
       list, int --> list
       Explicação: Guarda a concatenação da lista l e da lista contendo n numa variável lnova;
                   Ordena lnova de forma crescente através da função list.sort();
                   Guarda o índice de n em lnova numa variável i através da função list.index();
                   Retorna a fatia de lnova com os elementos de índice maior que o índice de n (já que estão em ordem crescente."""
    lnova = l + [n]
    lnova.sort()
    i = list.index(lnova, n)
    return lnova[i+1:]
#Teste 1:
#maiores([1, 2, 4, 5, 7, 9], 6)--> [7, 9]

#Teste 2:
#maiores([2, 45, 34, 440], 120)--> [440]
def acima_da_media(l):
    """"""
    media = sum(l)/len(l)
    if media in l:
        lnova = l
        lnova.sort()
        i = list.index(lnova, media
        return lnova[i+1:]
    else:
        notas_acima_da_media = maiores(l, media)
        return notas_acima_da_media