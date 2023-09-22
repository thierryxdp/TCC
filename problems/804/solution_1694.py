def pares_impares(n1,n2,n3,n4):
#essa função registra 4 numeros, os verifica e retorna somente os pares
#querido professor, ou monitor. Entendo que o modo que eu fiz a questão não correspondem com o momento atual da disciplina
#aprendi essas coisas enquanto adiantava a matéria acompanhando cursos gratuidos no youtube.

    lista_valores = [n1,n2,n3,n4]
    lista_pares = []

    for contador in range(0, len(lista_valores)):
        if(lista_valores[contador]%2 == 0):
            lista_pares.append(lista_valores[contador])

    return lista_pares