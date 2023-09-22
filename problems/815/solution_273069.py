def insere(lista_numero, n):
    """A função acima retorna uma nova lista ordenada de forma crescente.
       list, int -> list
       Explicação: A função converte o inteiro n em lista e o concatena com a lista_numero;
                   Essa concatenação é guardada na variável lnova ('lista nova');
                   lnova é ordenada de forma crescente através da função list.sort();
                   Assim, lnova é retornada."""
    lnova = lista_numero + [n]
    lnova.sort()
    return lnova
#Teste 1:
#insere([1, 2, 4, 5], 3)--> [1, 2, 3, 4, 5]

#Teste 2:
#insere([100, 200, 400], 300)--> [100, 200, 300, 400]

#Teste 3:
#insere([28, 35, 49], 42)--> [28, 35, 42, 49]