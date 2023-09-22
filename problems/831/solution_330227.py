def lingua_p(palavra):
    palavrinha = str.lower(palavra)
    
    for a in (palavrinha):
                lingua_a = str.replace(palavrinha,'a','apa')
    for e in (palavrinha):
                lingua_ae = str.replace(lingua_a,'e','epe')
    for i in (palavrinha):
                lingua_aei = str.replace(lingua_ae,'i','ipi')
    for o in (palavrinha):
                lingua_aeio = str.replace(lingua_aei,'o','opo')
    for u in (palavrinha):
                lingua_aeiou = str.replace(lingua_aeio,'u','upu')
    
    return lingua_aeiou