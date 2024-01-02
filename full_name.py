def combine_names(first_names, last_names):
    """
    Combine first names and last names into a list of full names.

    Parameters:
    - first_names (list): List of first names.
    - last_names (list): List of last names.

    Returns:
    - list: List of full names.
    """
    # Check if the lists have the same length
    if len(first_names) != len(last_names):
        raise ValueError("Lists must have the same length")

    # Use a list comprehension to combine first and last names
    full_names = [first + " " + last for first, last in zip(first_names, last_names)]
    return full_names

# Example usage:
first_names = ["John", "Jane", "Bob"]
last_names = ["Doe", "Smith", "Johnson"]

result_full_names = combine_names(first_names, last_names)
print(result_full_names)
