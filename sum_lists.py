def sum_lists(list1, list2):
    """
    Sum corresponding elements at each index of two lists.

    Parameters:
    - list1 (list): The first list.
    - list2 (list): The second list.

    Returns:
    - list: A new list containing the sum of corresponding elements.
    """
    # Check if the lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")

    # Use list comprehension to sum corresponding elements
    result = [x + y for x, y in zip(list1, list2)]
    return result

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result_list = sum_lists(list1, list2)
print(result_list)
