def busca(setor,lista):
    def verifica(lista):
        return True if setor in lista else False
    func= list(filter(verifica,lista))
    def exclui(fun):
        del(fun[2]) if setor in fun
            #del(fun[2])
    func2 = list(map(exclui, func))
    return func