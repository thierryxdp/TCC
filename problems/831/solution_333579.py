def lingua_p(palavra):
    '''exemplo --> epexepemplopo = e+p+(e)xe+p+(e)mplo+p+(o)
       então --> epentapaopo = e+p+(e)nta+p+(a)o+p+(o)
       caderno --> capadepernopo = ca+p+(a)de+p+(e)rno+p+(o)'''
    p=palavra.lower()
    s=''
    for c in p:
        if c in 'AEIOUaeiou':
            s+=c+'p'+c
        else:
            s+=c
    return s