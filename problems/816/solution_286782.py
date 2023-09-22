def empty(t):
    """Diz se /t/ é uma tupla vazia ou não.
    assinatura: tuple --> bool
    """
    return t == ()

def first(t):
    """Produz o primeiro elemento de /t/.
    assinatura: tuple --> any
    """
    if empty(t):
        raise exception("ilegal: first() em tupla vazia")
    else:
        return t[0]

def rest(t):
    """Produz o /t/ sem o primeiro elemento. Não pode ser tupla vazia.
    assinatura: tuple --> tuple
    """
    if empty(t):
        raise exception("ilegal: first() em tupla vazia")
    else:
        return t[1: ]

def cons(e, t): #cons/tructs a pair
    """ Constroi uma nova tupla colocando o elemento /e/ na cabeça de /t/
    assinatura: any, tuple --> tuple
    """
    return (e,) + t

def even(x):
    resto_da_divisao(x, 2) == 0
    
def odd(x):
    return not even(x)

def resto_da_divisao(a, b):
    a % b
    
from rec import*
    
def filtra(t, predicado):
    if empty(t):
        return ()
    if predicado(first(t)):
        return cons(first(t), filtra(rest(t)), predicado)
    else:
         return filtra(rest(t), predicado)
                    
def pred(n, x):
    return n < x
    
def filtra_pares(t):
    return filtra(t, even)
    
def filtra_impares(t):
    return filtra(t, odd)
    
def maiores(n, t):
    """Produz uma lista contendo elementos x de /ls/
    tal que n < x.
    assinatura: int, list --> list
    exemplos:
    maiores(4, ()) == ()
    maiores(1001, ()) == ()
    maiores(4, (11, 2, 3)) == (11,)
    maiores(0, (11, 2, 3)) == (11, 2, 3)
    
    Inventário:
    empty(ls)
    first(ls)
    rest(ls)
    cons(...,...)
    maiores(n, rest(ls))
    cons(..., maiores(n, rest(ls)))
    """
    if empty(t): #caso base
       return ()
    else: # caso recursivo, caso indutivo
       if n < first(t)
            return cons(first(t), maiores(n, rest(t))
       else:
            return maiores(n, rest(t))