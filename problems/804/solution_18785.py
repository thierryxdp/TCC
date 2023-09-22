def filtra_pares(tupla):
    """Função que retorna uma nova tupla contendo apenas elementos pares, dado um tupla com quatro elementos inteiros """
    nova_tupla = ()
    for i in range(len(tupla)):
        if tupla[i] % 2 == 0:
            nova_tupla = nova_tupla + (tupla[i],)
  	return nova_tupla