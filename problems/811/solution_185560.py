# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao([A,B,C],H,L):
       if A>H and B>L:
                return "false"
            else:
                if A>L and B>H:
                    return "false"
                elif A>H and C>H:
                     return "false"
                    elif A>L and C>H:
                         return "false"
                        elif B>H and C>L:
                             return "false"
                            elif B>L and C>H:
                                 return "false"
                                else:
                                    return "True"