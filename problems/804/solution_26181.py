def filtra_pares(t)
    lista = [] 
    if type(t) == tuple and len(t) == 4:
       for i in t:
           if type(i) != int:
              lista = [] 
              print('Todos os itens da tupla deveme ser inteiros.')
              break
            elif i%2 == 0:
                lista.append(i)
        print(tuple(lista))
    else:
        print('Apenas sera aceito, uma tupla, com quatro itens.')