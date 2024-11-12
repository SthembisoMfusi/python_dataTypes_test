def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    even_squares = []
    for i in range(21):
        if i%2 ==1 or i ==0:
            continue
        else:
            answer = i **2
            even_squares.append(answer)
    return even_squares

def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    student_grades = {}
    for i,j in students:
        student_grades[i] = j
    return student_grades


def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    c_dict = nested.get('c')
    c = c_dict.get('x')
    return c


def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    a_dict = nested.get('a')
    a_dict.append(6)
    return nested

nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    b_dict = nested.get('b')
    b_list = list(b_dict)
    b_list.append(6)
    nested['b'] = b_list
    return nested

