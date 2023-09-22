def melhor_volta(corredores: list[list[int]]) -> tuple[int]:
   '''Retorna uma tupla contendo o número do corredor que fez o melhor tempo, em
      que tempo fez e em que volta fez esse tempo'''
   #Criando lista de menores tempos
   menores_tempos = []
   #Criando listas de corredores candidatos a menores tempos
   candidatos = []

   # for que percorre os elementos (voltas) da lista corredores
   for volta in corredores:
      #Pegando o menor o tempo e adiciona na lista menores_tempos
      menorT = min(volta)
      menores_tempos.append(menorT)
      #Adiciona o número do corredor à lista de candidatos
      candidatos.append(volta.index(menorT))

   #for que percorre os índices da lista menores_tempos
   for ele in menores_tempos:
      #Verificando qual o menor tempo feito em todas as voltas
      if ele == min(menores_tempos):
         i = menores_tempos.index(ele)
         return (candidatos[i]+1,menores_tempos[i], i+1)