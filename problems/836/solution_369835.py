def busca(contatos, nome):
   lista = []
   for i in range(len(contatos)):
      if str.upper(nome) in str.upper(contatos[i][0]):
          list.append(lista,contatos[i])
   return lista