def lingua_p(palavra):
# Funcao que recebe como parametro uma string e retorna uma string que transforma a palavra inserida para a lingua do p
    palavrinha = str.lower(palavra)
    
    for a in (palavrinha):
                lingua_a = str.replace(palavrinha,'a','apa')
                lingua_ae = str.replace(lingua_a,'e','epe')
                lingua_aei = str.replace(lingua_ae,'i','ipi')
                lingua_aeio = str.replace(lingua_aei,'o','opo')
                lingua_aeiou = str.replace(lingua_aeio,'u','upu')
    			lingua_a1 = str.replace(lingua_aeiou,'á','ápá')
                lingua_ae1 = str.replace(lingua_a1,'é','épé')
                lingua_aei1 = str.replace(lingua_ae1,'í','ípí')
                lingua_aeio1 = str.replace(lingua_aei1,'ó','ópó')
                lingua_aeiou1 = str.replace(lingua_aeio1,'ú','úpú')
    return lingua_aeiou1