#Start your python function here
def pontos_por_time(lista):
    '''Recebe uma lista com a chave de duas partidas entre dois times e seu
resultado e retorna um discionário com os nomes dos times e seus pontos na
competição.
list --> dict'''
    time_pontos = {}
    jogo1 = lista[0]
    jogo2 = lista[1]
    time1_jogo1 , time2_jogo1 , result1 = jogo1
    time1_jogo2 , time2_jogo2 , result2 = jogo2
    time_pontos[time1_jogo1]  = 0
    time_pontos[time2_jogo1]  = 0
    
    if result1[0] > result1[1]:
        time_pontos[time1_jogo1] = 3
    elif result1[0] < result1[1]:
        time_pontos[time2_jogo1] = 3
    elif result1[0] == result1[1]:
        time_pontos[time1_jogo1] = 1
        time_pontos[time2_jogo1] = 1
    else:
        None

    if result2[0] > result2[1]:
        time_pontos[time1_jogo2] += 3
    elif result2[0] < result2[1]:
        time_pontos[time2_jogo2] += 3
    elif result2[0] == result2[1]:
        time_pontos[time1_jogo2] += 1
        time_pontos[time2_jogo2] += 1
    else:
        None
    return time_pontos

# Casos de teste

# pontos_por_time([['Cormengo','Flammınthians', [1, 0]], ['Flammınthians', 'Cormengo', [2, 2]]]) == {'Cormengo': 4, 'Flammınthians': 1}
# pontos_por_time([['Cormengo','Flammınthians', [0, 0]], ['Flammınthians', 'Cormengo', [2, 2]]]) == {'Cormengo': 2, 'Flammınthians': 2}
# pontos_por_time([['Cormengo','Flammınthians', [1, 0]], ['Flammınthians', 'Cormengo', [2, 0]]]) == {'Cormengo': 3, 'Flammınthians': 3}
# pontos_por_time([['Cormengo','Flammınthians', [1, 0]], ['Flammınthians', 'Cormengo', [0, 2]]]) == {'Cormengo': 6, 'Flammınthians': 0}