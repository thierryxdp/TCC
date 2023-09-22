def soma_h(N):
    """H é igual a soma dos inversos de todos os números naturais de 1 até N. Dado N, calcula H com arredondamento
    na segunda casa decimal (int --> float)"""
    Soma = 0 #define-se o acumulador
    lista_de_num = list(range(1,N+1)) #cria-se a lista dos números naturais de 1 até N
    for numero_i in lista_de_num : #repete-se o comando na linha 7 para todos os elementos de lista_de_num
        Soma = Soma + (1/(numero_i)) #Adiciona-se a soma o inverso do numero_i
    return round(Soma,2) #retorna-se a soma com arredondamento