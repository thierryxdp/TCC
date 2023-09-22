def melhor_volta(mat_kart):
    '''Essa funcao recebe de entrada uma matriz 6x10 com os 
    tempos em segundos de cada corredor em cada volta.
    As linhas agrupam os tempos de cada corredor e as 
    colunas representam as voltas.
    O retorno eh de quem foi a melhor volta da prova 
    (melhor corredor), o melhor tempo e em qual volta 
    isso ocorreu.
  	matriz (int) -> int, int, int'''

    melhor_corredor = -1 #extrapolar valores que nunca poderiam assumir para
    melhor_t = -1       #iniciar o codigo
    em_qual_volta = -1
    menores_tempos = []

    for corredor in mat_kart:
        list.append(menores_tempos,min(corredor))
    melhor_t = min(menores_tempos)

    ind = 0 #vai ser usado para contar os corredores
    for corredor in mat_kart:
        ind = ind + 1 # aqui ja eh o primeiro corredor
        if melhor_t in corredor:
            melhor_corredor = ind
            em_qual_volta = list.index(corredor, melhor_t) + 1 #contando as voltas e add 1 pq o indice comeca em 0

    return melhor_corredor, melhor_t, em_qual_volta
            
#Casos de teste
#teste com apenas 3 corredores para verificar o funcionamento da funcao
# voltas1 = [[1,2,3],[4,5,6],[7,8,9]]
# melhor_volta(voltas1) == (1, 1, 1)

# voltas2 = [[4,5,6],[3.2,3,2.5],[7,8,9]]
# melhor_volta(voltas2) == (2, 2.5, 3)

# voltas3 = [[4,5,6],[7,8,9],[1,2,3]]
# melhor_volta(voltas3) == (3, 1, 1)

# voltas4 = [[4,5,6],[1,2.1,0.9],[7,8,9]]
# melhor_volta(voltas4) == (2, 0.9, 3)

# voltas4 = [[4,5,6],[7,8,9],[3,2,1]]
# melhor_volta(voltas4) == (3, 1, 3)