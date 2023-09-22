def lingua_p (palavra):
    '''
    Fução que recebe uma palavra e a "traduz" para a
    linguagem do P.
    Uma palavra é traduzida para a lingugem do P quando,
    apos cada vogal da palavra original, é inserida a sequencia
    de letras 'p' mais a vogal original
    string--->string
    '''
    p=str.lower(palavra)
    p1=str.replace(p,a,apa)
    p2=str.replace(p1,e,epe)
    p3=str.replace(p2,i,ipi)
    p4=str.replace(p3,o,opo)
    p5=str.replace(p4,u,upu)
    return p5