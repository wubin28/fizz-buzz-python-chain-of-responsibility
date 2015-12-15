
class Fizzbuzz:

    def say(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"

        handlerFizzbuzz = HandlerFizzbuzz(handlerFizz)
        result = handlerFizzbuzz.handle(number)

        return str(number)

class HandlerFizzbuzz(Handler):

    def handleFizzbuzz(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        
