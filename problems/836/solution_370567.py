def busca(contatos, nome):
   """função que recebe uma lista de contatos e um nome referente ao nome
   buscado e retorna uma lista de contatos que tem o nome buscado.
   list, str -> list"""
   i = 0
   lista = []
   while i < len(contatos):
      if nome in (contatos[i][0]):
          lista.append(i[0])
          lista.append(i[1])
          lista.append(i[3])
      i = i + 1
   return lista