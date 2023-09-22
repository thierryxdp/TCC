def lingua_p(palavra):
    for a in palavra:
        if a == 'a':
            palavraa = palavra.replace('a','apa')
            for e in palavraa:
                if e == 'e':
                    palavrae = palavraa.replace('e','epe')
                    for i in palavrae:
                         if i == 'i':
                            palavrai = palavrae.replace('i','ipi')
                            for o in palavrai:
                                    if o == 'o':
                                        palavrao = palavrai.replace('o','opo')
                                        for u in palavrao:
                                            if u == 'u':
                                                palavrau = palavrao.replace('u','upu')
                                            return(palavrau)