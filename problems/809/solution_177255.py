def intercala(L1, L2):
    """Ao receber duas listas L1 e L2 como parâmetro, a função acima retorna outra
       lista formada com os elementos de entrada.
       lista, lista -> lista
       Explicação: A função concatena as listas L1 e L2 fatiando seus elementos 
       de modo que cada fatia contém um único termo. Assim, é gerada uma nova 
       lista com as fatias de L1 e L2 intercaladas."""
    x = L1[:1] + L2[:1]
    y = L1[1:2] + L2[1:2]
    z = L1[2:] + L2[2:]
    return x + y + z

#Teste 1:
#intercala([1, 3, 5], [2, 4, 6])--> [1, 2, 3, 4, 5, 6]

#Teste 2:
#intercala(['Rihanna', 'e', 'resto'], ['rainha', 'o', 'nadinha'])--> ['Rihanna', 'rainha', 'e', 'o', 'resto', 'nadinha']

#Teste 3:
#intercala([['O'], ['não'], ['o']], [['sapo'], ['lava'],['pé']])--> [['O'], ['sapo'], ['não'], ['lava'], ['o'], ['pé']]