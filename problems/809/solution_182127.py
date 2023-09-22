def Exercicio1(L1,L2):
    N1 = len(L1)
    N2 = len(L2)
    #---------------------------------
    print "INTERCALACAO DE ELEMENTOS NUMA LISTA"
    print "------------------------------------"
    print "Sejam as listas L1 e L2"
    print "     ",L1
    print "     ",L2
    #---------------------------------
    if (N1==3):
       if N2==3:
          L3 = []
          for i in range(N1):
              L3.append(L1[i])
              L3.append(L2[i])
          print "A lista intercalas é"
          print "     ",L3)
       else:
          print "ERRO: A Lista L2 nao tem tamanho 3"
    else:
      print "ERRO: A Lista L1 nao tem tamanho 3"