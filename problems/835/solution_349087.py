def insertion_sort(lista: List):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(lista)):
        item_to_insert = lista[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and lista[j] > item_to_insert:
            lista[j + 1] = lista[j]
            j -= 1
        # Insert the item
        lista[j + 1] = item_to_insert
    return lista