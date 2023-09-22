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
    p1=str.replace(p,'a','apa')
    p2=str.replace(p1,'e','epe')
    p3=str.replace(p2,'i','ipi')
    p4=str.replace(p3,'o','opo')
    p5=str.replace(p4,'u','upu')
    p6=str.replace(p5,'é','épé')
    p7=str.replace(p6,'á','ápá')
    p8=str.replace(p7,'ú','úpú')
    return p8