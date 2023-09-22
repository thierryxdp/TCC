def zodiaco(ano):
    """função que dado o ano de nascimento de uma pessoa, retorna seu signo  aproximado correspondente"""
calculo_signo = ano_nascimento%12
return ("macaco", "galo", "cão", "porco", "rato", "boi", "tigre", "coelho", "dragão", "serpente", "cavalo", "carneiro")[calculo_signo]