def colchao(lista, h,l):
   '''Esta função retorna se o colchão conseguirá passar pelas portas. Sendo:
   h-> altura do colchão
   l-> largura do colchão'''
   '''list-> int,int,int'''
    if h<lista[1] and  l<lista[2]:
        return False
    else:
        return True