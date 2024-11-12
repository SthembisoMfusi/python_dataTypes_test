def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    answer = 7 //2
    return answer

def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    num1 = float(3)
    num2 = 2
    answer = num1 * num2
    return answer 


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    result = float_multiplication() + int_division()
    return result


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = 'Python is awesome!'
    if 'awesome' in string:
        return 'awesome'


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    low = string.lower()
    return low


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    string = 'Python is awesome!'
    counter = string.count('o')
    return counter


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    pass
