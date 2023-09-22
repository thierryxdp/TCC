def qtd_divisores(i):
    l = []
    for n in range(1, i):
        if i % n == 0:
            list.append(l, n)
        if i not in l:
            list.append(l, i)
    return len(l)
def primo(i):
    """A função verifica se o inteiro dado como parâmetro é um número primo ou não.
       int -> bool"""
    if qtd_divisores(i) == 2:
        return True
    else:
        return False
#Testes:
#primo(17)--> True 
#primo(2)--> True
#primo(12)--> False
#primo(313)--> True
#primo(15)--> False