def intercala(Lista1,Lista2):
    N1 = len(Lista1)
    N2 = len(Lista2)
    #---------------------------------
    print "INTERCALACAO DE ELEMENTOS NUMA LISTA"
    print "------------------------------------"
    print "Sejam as listas Lista1 e Lista2"
    print "     ",Lista1
    print "     ",Lista2
    #---------------------------------
    if (N1==3):
       if N2==3:
          L3 = []
          for i in range(N1):
              L3.append(Lista1[i])
              L3.append(Lista2[i])
          print "A lista intercalas é"
          print "     ",L3)
       else:
          print "ERRO: A Lista Lista2 nao tem tamanho 3"
    else:
      print "ERRO: A Lista Lista1 nao tem tamanho 3"
#===========================================================
A=[22,44,788]
B=[33,88,99]
Exercicio1(A,B)