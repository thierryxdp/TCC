def insere(lista_numero, n):
    """ recebe uma lista de números e um número que deve ser adicionado nessa lista de forma que retorne uma lista com esse número e em ordem crescente.
    list,int -> list
    Explicação: basta receber o número novo e inseri-lo na sequencia e em seguida ordená-la crescentemente."""
    list.insert(lista_numero, n, n)
    list.sort(lista_numero)
    return lista_numero
# teste 1
# insere([1,2,3],7)
# saida esperada: [1,2,3,7]
# teste 2
# insere([1,1,1,6],5)
# saida esperada: [1,1,1,5,6]