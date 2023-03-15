def linear(input_list, search_term):
    """In case you don't feel like using .index()"""
    for index in input_list:
        if index == search_term:
            return index
    return None

def linear_all(input_list, search_term):
    return [index for index in range(len(input_list)) if input_list[index] == search_term]
