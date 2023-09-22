def busca(setor, contatos):
   """função que recebe uma lista de contatos e um nome referente ao nome
   buscado e retorna uma lista de contatos que tem o nome buscado.
   list, str -> list"""
   novaLista = []
   for i in range(len(matriz)):
        lista = []
        for j in i:
            if j == setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
                novaLista.append(lista)
   return novaLista