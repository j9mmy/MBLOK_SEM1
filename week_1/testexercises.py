from time import sleep
import sys
import numpy as np
OKGREEN = '\033[92m'
ENDC = '\033[0m'

#################################################
# helper functions
#################################################
def correct_assertion():
    print(f"\n{OKGREEN}All tests passed!!!"+ ENDC)

def loader():
    for i in range(10):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        sleep(0.1)

#################################################
# exercise tests
#################################################

# Area rectancle

def hint_area_rectangle():
    print("We can store and calculate the area of a rectangle by using:\n`result = length * width`.")

def test_area_rectangle(f):
    loader()
    assert(f(3, 4) == 12)
    correct_assertion()

# Convert Fahrenheit to celsius

def hint_fahr_to_cel():
    print("celsius = (fahrenheit - 32) * 5/9 and also make sure you return the value so the test can see if its correct")

def test_fahr_to_cel(f):
    loader()
    assert(f(41) == 5.0)
    assert(f(-4) == -20.0)
    correct_assertion()

# Count A names

def hint_count_A_names():
    print("We can use a for loop to loop over all the names like: for name in names:")
    print("We can then check if the first letter of the name starts with an A by getting the index of the first letter: name[0]")

def test_count_A_names(f):
    loader()
    assert(f(["Alice", "Bob", "Amy", "Alex"]) == 3)
    assert(f(["Alice", "Bob"]) == 1)
    assert(f(["Bob"]) == 0)
    correct_assertion()

# getting the average

def hint_get_average():
    print("we can loop over all the number and add it up to a total, after getting the total we can do a division like total/len(numbers) to get the average")

def test_get_average(f):
    loader()
    assert(f([1,2,3,4,5]) == 3.0)
    assert(f([1,2,7,5]) == 3.75)
    correct_assertion()

def hint_first_last_letter():
    print("Remember we can acces the last letter by using text[-1]")
    print("also note we can add 2 string together by using a +")

def test_first_last_letter(f):
    loader()
    assert(f("test") == "tt")
    assert(f("next") == "nt")
    correct_assertion()

def hint_reverse_string():
    print("Have you thought about looping over the text? If your lazy you might figure out what [::-1] does.")

def test_reverse_string(f):
    loader()
    assert(f("test") == "tset")
    assert(f("correct") == "tcerroc")
    correct_assertion()

def hint_is_palindrome():
    print("We can use the same logic as the previous exercise and check if its equal to the input.")

def test_is_palindrome(f):
    loader()
    assert(f("test") == False)
    assert(f("racecar") == True)
    correct_assertion()

def hint_in_list():
    print("you can check if the string is in the list_obj by using the `in` operator")

def test_in_list(f):
    loader()
    assert(f(["test", "hello"], "hello") == True)
    assert(f(["test", "hello"], "notin") == False)
    correct_assertion()

def hint_custom_sort_list():
    print("You can zip the 2 list together using the zip function.")
    
def test_custom_sort_list(f):
    loader()
    assert(f(["3", "test", "2", "1"], [3, 0, 2, 1]) == ["1", "3", "2", "test"])
    correct_assertion()

def hint_matrixmul():
    print("you can use the @ operator to do the matmul")

def test_matrixmul(f):
    loader()
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7,8], [9,10], [11,12]])
    result = matrix1 @ matrix2
    assert(np.array_equal(f(matrix1, matrix2), result))
    correct_assertion()

def hint_matrix3x3():
    print("we can use arange and afterwards a reshape")

def test_matrix3x3(f):
    loader()
    matrix = np.arange(2,11).reshape(3,3)
    assert(np.array_equal(f(), matrix))
    correct_assertion()

def hint_append_array():
    print("you can use np.append()")

def test_append_array(f):
    loader()
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    result = np.append(x, y)
    assert(np.array_equal(f(x, y), result))
    correct_assertion()

def hint_checkerboard_pattern():
    print("first we can initialize our board using board = np.zeros((y, x), dtype=int)")
    print("then we can use some smart index to assign 1 using:")
    print("board[1::2, ::2] = 1")
    print("board[::2, 1::2] = 1")

def test_checkerboard_pattern(f):
    loader()
    x = 5
    y = 5
    result = np.zeros((y, x), dtype=int)
    result[1::2, ::2] = 1
    result[::2, 1::2] = 1
    assert(np.array_equal(f(5, 5), result))
    correct_assertion()

def checkerboard_pattern(x, y):
    board = np.zeros((y, x),dtype=int)
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    return board

# checkerboard_pattern(4, 6)

