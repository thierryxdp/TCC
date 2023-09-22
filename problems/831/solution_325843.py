def lingua_p(palavra):
    for i<len(palavra):
        if i in 'aeiou':
            if i=='a':
                str.replace(palavra,'a','apa')
                if i=='e':
                    str.replace(palavra,'e','epe')
                    if i=='i':
                        str.replace(palavra,'i','ipi')
                        if i=='o':
                            str.replace(palavra,'o','opo')
                            if i=='u':
                                str.replace(palavra,'u','upu')
        return palavra