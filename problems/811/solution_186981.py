import re 
def substitui(texto):
    substituido = re.sub(r'[^\w\s]', '', texto)

    return substituido