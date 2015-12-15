
class Fizzbuzz:

    def say(self, number):
        handlerNormalNumber = HandlerNormalNumber(None)
        handlerBuzz = HandlerBuzz(handlerNormalNumber)
        handlerFizz = HandlerFizz(handlerBuzz)
        handlerFizzbuzz = HandlerFizzbuzz(handlerFizz)
        result = handlerFizzbuzz.handle(number)

        if number % 15 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"

        return str(number)


class Handler:

    def __init__(self, successor = None):
        self.__successor = successor


class HandlerFizzbuzz(Handler):

    def handle(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        self.__successor.handle(number)
        

class HandlerFizz(Handler):

    def handle(self, number):
        if number % 3 == 0:
            return "Fizz"
        super(HandlerFizz, self).__successor.handle(number)
        
class HandlerBuzz(Handler):

    def handle(self, number):
        if number % 5 == 0:
            return "Buzz"
        super(HandlerBuzz, self).__successor.handle(number)
        
class HandlerNormalNumber(Handler):

    def handle(self, number):
        return str(number)
        
