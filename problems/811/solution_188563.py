def passa_pela_porta(faces_do_colchao,h,l):
    """Dado as dimensões a,b e c de um colchão em ordem crescente, a altura h e
    largura l de uma porta, retorna se é possível que o colchão passe por ela:
    list[int,int,int],int,int-->bool"""
    menor_face1=faces_do_colchao[0]
    menor_face2=faces_do_colchao[1]
    if (( menor_face1<=h)or(menor_face1<=l))and((menor_face2<=h)or(menor_face2<=l)):
        return True
    else:
        return False