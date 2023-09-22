def lingua_p(palavra):
    """ Recebe como parâmetro uma palavra (em português) e retorna esta mesma palavra traduzida para a língua do P. Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original.
    str-->str"""
    s=list(palavra)
    i=0
    for i in range(0,len(s)+palavra.count("a")+palavra.count("e")+palavra.count("i")+palavra.count("o")+palavra.count("u")):
        if s[i]=="a":
            s.insert(i+1,"pa")
        if s[i]=="e":
            s.insert(i+1,"pe")
        if s[i]=="i":
            s.insert(i+1,"pi")
        if s[i]=="o":
            s.insert(i+1,"po")
        if s[i]=="u":
            s.insert(i+1,"pu")
        if s[i]=="ã":
            s.insert(i+1,"pã")
        if s[i]=="é":
            s.insert(i+1,"pé")
        if s[i]=="á":
            s.insert(i+1,"pá")
        if s[i]=="ú":
            s.insert(i+1,"pú")
    a=""
    return str.lower(str.join(a,s))