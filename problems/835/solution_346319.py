def melhorvolta(m):
    '''Dada uma matriz com os 10 tempos de cada um dos 6 corredores,
       a função retorna qual foi a volta com o melhor tempo, qual esse
       tempo e quem o fez
       list -> list
       Parametros:
       m: matriz a ser digitada'''
    mc = 0
    mv = 0
    retorno = 0
    l = []
    mt = min(float(m[0]))
    for c in range(1, 6):
        for p in range(0, 10):
            mt = min(mt, float(m[c])
  	for i in range(0, 6):
   		for s in range(0, 10):
          	if mt in m[i][s]:
                   	list.append(l, i)
                    list.append(l, mt)
                   	list.append(l, s)
                 	return l