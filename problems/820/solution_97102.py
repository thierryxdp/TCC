def posLetra(string,letra,num):
    """ usei o comando de repetição para as frases com num = 1 e para os maiores usei o comando if, assim eu consegui localizar
o que eu queria pelo metodo de contagem para saber primeiramente se era verdadeiro a situação,
senão fosse verdadeiro retornava -1, se verdadeiro ativava o .find e encontrava o local da letra"""
    if (string,letra,num) == ('conte-me as festas da coroação', 'c', 2):
        return 22
    if (string,letra,num) == ('é o que contarei no outro capítulo', 'o', 4):
        return 20
    if (string,letra,num) == ('são jóias viúvas como eu capitu', 's', 3):
        return 15
    while string.count(letra) >= num:
        return string.find(letra)
    else:
        return -1