

def generate_pyramid(n,char:str='*'):
    """
    Prints a pyramid of characters, by default, asterisks (*) of height n.

    The pyramid will be centered, and will have a height of n, with each
    row being 2 * n - 1 characters long. The default character used is *
    but a different character can be specified with the char argument.

    Parameters
    ----------
    n : int
        The height of the pyramid.
    char : str, optional
        The character to use in the pyramid. Must be a single character.

    Raises
    ------
    ValueError
        If n is not between 1 and 20, or if char is not a single character.

    Examples
    --------
    >>> generate_pyramid(3)
      *
     ***
    >>> generate_pyramid(4,'#')
       #
      ###
     #####
    #######
    """
    # print(f'[DEBUG] : {n=},{char=}') # Debug statement to check the values of n and char

    # checkings
    if n<1 or n>20:
        raise ValueError('n must be between 1 and 20')
    if type(n) != int:
        raise TypeError('n must be an integer')
    if len(char) != 1 and char not in ['\'','\"']:
        raise ValueError('char must be a single character')
    
    # print the pyramid, centered
    for i in range(1,n+1):
        chars = char * (2 * i - 1)
        spaces = ' ' * (n - i)
        print(spaces + chars + spaces)
        

if __name__ == '__main__':
    generate_pyramid(5)
    generate_pyramid(3,'#')
    generate_pyramid(10,'@')