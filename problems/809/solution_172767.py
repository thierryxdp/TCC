def intercala(lista1,lista2):
    """Dada duas listas L1 e L2 com o tamanho 3, gera uma lista L3 que é formada intercalando os elementos da L1 e L2
    Os paramêtro de entrada são list, list
    O retorno esperado é list"""
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]
for i in range(len(lista2)):
 lista1.append(lista2[i])
print(lista1)
for i in range(len(lista1)):
  lista2.append(lista[j])
print(lista2)