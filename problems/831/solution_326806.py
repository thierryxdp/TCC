def lingua_p(x):
    x = x.lower()
    word = []
    for i in range(len(x)):
        if (x[i] == 'a' or 'e' or 'i' or 'o' or 'u'):
            word.append('p')
            word.append(x[i])
        else:
            word.append(x[i])