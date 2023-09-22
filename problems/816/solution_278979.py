def maiores(num_list, n):
    new_list = []
    for i in range(len(num_list)):
        if n < num_list[i]:
            new_list.append(num_list[i])
    return new_list