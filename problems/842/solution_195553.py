def pontos_por_time (lista):
    '''Instruções: Os dois elementos da lista, são também listas, veja o exemplo de como inserir o valor:
    Exemplo: [[time1,time2,[gols1,gols2]],[time2,time1,[gols2,gols1]]]'''
#Definindo times
	t = lista[0:1]
	time1 = t[0:1]
	time2 = t[1:]
	return time1