def busca(contatos, nome):
   """função que recebe uma lista de contatos e um nome referente ao nome
   buscado e retorna uma lista de contatos que tem o nome buscado.
   list, str -> list"""
   lista = []
   for i in range(len(contatos)):
      if str.upper(nome) in str.upper(contatos[i][0]):
          list.append(lista,contatos[i])
   return lista