def intercala(lista1,lista2):
     '''Funcao que retorna uma terceira lista
     intercalando duas listas de entrada.
     Dados de entrada: list, list
     Valor de saida: list
     '''               
     lista3 = []
     for a,b in zip(lista1,lista2):
         lista3.append(a)
         lista3.append(b)
         return lista3