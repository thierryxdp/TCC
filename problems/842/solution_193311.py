def classificacao(cv, ce, cs, fv, fe, fs):
    ''' Retorna como resultado, vitória, empates e saldo de gols dos dois times'''
    '''int, int, int ,int ,int, int -> string'''

    pc = cv*3+ce
    pf = fv*3+fe
    
    if pc > pf:
       return 'Cormengo'
    elif pf > pc:
         return 'Flaminthians'
    else:
         if cs > fs:
           return 'Cormengo'
         elif fs > cs:
           return 'Flaminthians'
         elif cs == fs:
           return 'Empate'