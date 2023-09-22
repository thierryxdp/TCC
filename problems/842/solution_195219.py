def pontos_por_time(lista):

    """
        Função que recebe uma lista contendo duas sub-listas e retorna um dicionario.
        
        (1) As sub-listas tem como elementos 0 e 1 nomes de times e o elemento 2 (uma outra sub-lista) o placar do jogo entre os times listados no elemento 0 e 1.
            ex:
               sub-lista --> ["vasco","flamengo",[0,0]] ==> Isso significa que houve um jogo no qual o vasco enfrentou o flamengo e o resultado final foi 0 a 0
               
        (2) A lista de entrada da função representa o jogo de ida e o jogo de volta.
            ex:
                lista --> [["vasco","flamengo",[0,0]],["flamengo","vasco",[1,0]]] ==> Isso signigica que houve um jogo entre flamengo e vasco, no jogo de ida
                o vasco era o mandante e o placar foi de 0 a 0, já no jogo de volta o flamengo era o mandante e o placar foi de 1 a 0.
                
        (3) Para cada resultado vai existir uma quantidade de pontos relacionado, veja a lista abaixo:

                empata = Cada time ganha 1 ponto
                vitoria = O time que ganhar recebe 3 pontos
                Perda = O time que perder não vai receber nenhuma pontuação.

        (4) A função vai retornar um ducionario contendo como chave os nomes dos times e associada a essa chave a pontuação total que o time fez (ponto do jogo de
            ida + ponto do jogo da volta).

            ex: lista --> [["vasco","flamengo",[0,0]],["flamengo","vasco",[1,0]]].

                            Jogo de ida ==> vasco x flamengo: 0 a 0 --> Cada time fez 1 ponto (empate) 
                            Jogo de volta ==> flamengo x vasco 1 a 0 --> O flamengo fez 3 pontos (vitorioso) e o vasco não fez nenhum ponto (não obteve vitoria)

            Pode ser observado que no código da função existe uma váriavél chamada times, ela que vai ser retornada no final da função. No caso do nosso exemplo:

                            valor retornado = {"vasco":1,"flamengo":4}
                
        list --> dict
    """

    
    times = {lista[0][0]:0, lista[0][1]:0}


    for i in lista:
        if i[2][0] == i[2][1]:
            times[lista[0][0]] += 1
            times[lista[0][1]] += 1
        else:
            if i[2][0] > i[2][1]:
                times[i[0]] += 3
            elif i[2][0] < i[2][1]:
                times[i[1]] += 3
    return times