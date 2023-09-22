def intercala(lista1,lista2):
    N1 = len(lista1)
    N2 = len(lista2)
    #---------------------------------
    print("INTERCALACAO DE ELEMENTOS NUMA lista")
    print("------------------------------------")
    print("Sejam as listas lista1 e lista2")
    print("     ",lista1)
    print("     ",lista2)
    #---------------------------------
    if (N1==3):
       if N2==3:
          L3 = []
          for i in range(N1):
              L3.append(lista1[i])
              L3.append(lista2[i])
          print("A lista intercalas é")
          print("     ",L3)
       else:
         print("ERRO: A lista lista2 nao tem tamanho 3")
    else:
      print("ERRO: A lista lista1 nao tem tamanho 3")