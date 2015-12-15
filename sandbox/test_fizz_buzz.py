import fizz_buzz_kata

def test_it_should_print_the_number_itself_if_it_is_a_normal_number():
    # arrange
    fizzbuzz = fizz_buzz_kata.Fizzbuzz()

    # act & assert
    assert fizzbuzz.say(1) == "1"

def test_it_should_print_Fizz_if_it_is_multiple_of_three():
    # arrange
    fizzbuzz = fizz_buzz_kata.Fizzbuzz()

    # act & assert
    assert fizzbuzz.say(3) == "Fizz"

def test_it_should_print_Buzz_if_it_is_multiple_of_five():
    # arrange
    fizzbuzz = fizz_buzz_kata.Fizzbuzz()

    # act & assert
    assert fizzbuzz.say(5) == "Buzz"

def test_it_should_print_FizzBuzz_if_it_is_multiple_of_both_three_and_five():
    # arrange
    fizzbuzz = fizz_buzz_kata.Fizzbuzz()

    # act & assert
    assert fizzbuzz.say(15) == "FizzBuzz"

