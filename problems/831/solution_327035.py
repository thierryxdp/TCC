def lingua_p(string):
    for i in range(len(string)):
        if string[i]=="AaEeIiOoUuãÃéÉíÍóÓúÚáÁ":
            string=string[i]+'p'+string[i]
            return string