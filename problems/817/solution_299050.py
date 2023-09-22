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
    """Dada uma lista com as notas dos alunos de uma turma, a função calcula,
       interpreta e retorna uma lista contendo a(s) nota(s) de l maior(es) que a média 
       das notas de l.
       list -> list
       Explicação: Com a função sum(), calcula-se a média das notas de l;
                   Com o auxílio da função antes definida 'maiores()', a função 'acima_da_media' retorna a lista desejada;
                   Caso o valor da média seja igual a um elemento de l, lnova = l. Caso contrário, se lnova = l + [n],
                   sendo n correspondente a média, teremos um elemento repetido na lista, o que atrapalharia a contagem dos índices;
                   Caso a média não pertença a l, lnova = l + [n]"""
                   
    media = sum(l)/len(l)
    notas_acima_da_media = maiores(l, media)
    if media in l:
        lnova = l
        lnova.sort()
        i = list.index(lnova, media)
        return lnova[i+1:]
    else:
        return notas_acima_da_media
#Teste 1:
#acima_da_media([5, 7, 10, 4])--> [7, 10]

#Teste 2:
#acima_da_media([3.5, 7, 8])--> [7, 8]