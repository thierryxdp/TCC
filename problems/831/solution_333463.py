def lingua_p(palavra):
    for a in palavra:
        if a == 'a':
            palavraa = palavra.replace('a','a'+'p'+'a')
            for e in palavraa:
                if e == 'e':
                    palavrae = palavraa.replace('e','e'+'p'+'e')
                    for i in palavrae:
                         if i == 'i':
                             palavrai = palavrae.replace('i','i'+'p'+'i')
                             for o in palavrai:
                                  if o == 'o':
                                      palavrao = palavrai.replace('o','o'+'p'+'o')
                                      for u in palavrao:
                                           if u == 'u':
                                               palavrau = palavrao.replace('u','u'+'p'+'u')
    return(palavrau)