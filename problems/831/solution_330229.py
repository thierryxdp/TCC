def lingua_p(palavra):
    palavrinha = str.lower(palavra)
    
    for a in (palavrinha):
                lingua_a = str.replace(palavrinha,'a','apa')
                lingua_ae = str.replace(lingua_a,'e','epe')
                lingua_aei = str.replace(lingua_ae,'i','ipi')
                lingua_aeio = str.replace(lingua_aei,'o','opo')
                lingua_aeiou = str.replace(lingua_aeio,'u','upu')
    			lingua_a1 = str.replace(lingua_aeiou,'á','ápa')
                lingua_ae1 = str.replace(lingua_a1,'é','épe')
                lingua_aei1 = str.replace(lingua_ae1,'í','ípi')
                lingua_aeio1 = str.replace(lingua_aei1,'ó','ópo')
                lingua_aeiou1 = str.replace(lingua_aeio1,'ú','úpu')
    return lingua_aeiou1