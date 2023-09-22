def substitui(s: str, x: str, i: int) -> str:
    """Substitui uma caractere da string por outra

       Parameters:
       s: String a ser modificada entre parênteses
       x: Caractere a ser incluído na string entre parênteses
       i: Número inteiro que representa a posição da string que vai ser
       modificada

       Return:
       Uma string igual ao parâmetro "s", exceto que o elemento da posição
       determinado pelo parâmetro "i" será substituido pelo caractere
       do parâmetro "x"

       Examples:
       substitui("ola", "k", 1) == 'oka'
       substitui("parabens", "#", 4) == 'para#ens'
       substitui("computacao", "@", 6) == 'comput@cao'
    """
    
    a = s[:i]
    b = s[i+1:]

    return a + x + b