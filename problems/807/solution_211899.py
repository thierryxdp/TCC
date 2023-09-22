def conta_frases(texto):
    '''Função que calcula o número de frases presentes em um texto; str -> int'''
frasesinterrogativas = str.count(texto,?)
frasesafirmativas = str.count(texto,.)
frasesexclamacao = str.count(texto,!)
frasesreticencias = str.count(texto,...)
    return frasesinterrogativas + frasesafirmativas + frasesexclamacao + frasesreticencias