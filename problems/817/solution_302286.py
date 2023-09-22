def acima_da_media(lista):
    """Recebe uma referencia de lista de notas e retorna apenas as que estao acima da media da turma;
    list<float>[???] --> None"""
    media = (sum(lista)/len(lista))

    maiorQ(lista, media)