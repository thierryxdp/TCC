def busca(contatos, nome):
   lista = []
   for i in range(len(contatos)):
      if str.upper(contatos[i][2]) in str.upper(nome):
        list.append(lista,contatos[i])
   return lista