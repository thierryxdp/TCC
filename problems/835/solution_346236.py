def melhorvolta(m):
    '''Dada uma matriz com os 10 tempos de cada um dos 6 corredores,
       a função retorna qual foi a volta com o melhor tempo, qual esse
       tempo e quem o fez
       list -> list
       Parametros:
       m: matriz a ser digitada'''
    mc = mv = 0
    mt = min(float(m[0].split()))
    for c in range(1, 6):
        for p in range(0, 10):
            mt = min(mt, float(m[c])) 
    return mt