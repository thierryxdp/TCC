def lingua_p(x):
    vogal=('a','e','i','o','u')
    for i in range(len(x)):
        if i in vogal:
            return i+'p'+i
        else:
            return i