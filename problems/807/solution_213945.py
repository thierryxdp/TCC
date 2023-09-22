def contafrases(texto):
    return str.count(texto,'.',[0:])+str.count(texto,'!',[0:])+str.count(texto,'?',[0:]-str.count(texto,'...',[0:])