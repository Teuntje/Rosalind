import random

def number_of_permutations(integer):
    """Bereken de hoeveelheid permutaties mogelijk voor deze int"""
    fact = 1
    for i in range(1, integer+1):
        fact = fact*i
    return fact


def permutation(integer, number):
    """Verkrijg alle lijsten met nummers in alle mogelijke manieren

    input:
    integer - int - het nummer
    number - int - het aantal manieren om het te doen

    output:
    permutation-possibilities - list - aantal mogelijke volgorden bij
    elkaar in een lijst
    """
    permutation_possibilities = []
    new_permutation = []
    for i in range(1, integer+1):
        new_permutation.append(i)

    permutation_possibilities.append(new_permutation)

    while len(permutation_possibilities) < number:
        new_random_list = random.sample(new_permutation, len(new_permutation))
        
        if new_random_list not in permutation_possibilities:
            permutation_possibilities.append(new_random_list)
            new_random_list = []

    return permutation_possibilities


def pretty_print(number, pos):
    """pretty print function"""
    print(number)
    for i in pos:
        string_ints = [str(int) for int in i]
        str_of_ints = " ".join(string_ints)
        print(str_of_ints)


if __name__=="__main__":
    integer = 7
    number = number_of_permutations(integer)
    pos = permutation(integer, number)
    pretty_print(number, pos)
    
                
