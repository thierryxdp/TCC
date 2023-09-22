def intercala(lista1,lista2):
     '''Funcao que retorna uma terceira lista
     intercalando duas listas de entrada.
     Dados de entrada: list, list
     Valor de saida: list
     '''               
     lista3 = []
     for i in zip(lista1,lista2):
         lista3.append(lista1)
         lista3.append(lista2)
         return lista3