def greetMessage(name):
   
    # if input is a number, error
    if (not isinstance(name, str)):
        raise Exception('Wrong data type provided!')
    
    # if no input provided, error
    if (not name or name.isspace()):
        raise Exception('Provide better data!')
    
    if (not name.isalpha()):
        raise Exception('Need some letters in your name!')

    # assume input is a string and return a new string
    return f'Hello there, {name}!'

# print(greetMessage('Alex'))
# print(greetMessage('300'))
# print(greetMessage({}))


import random
from randomJokesList import randomJokes

def getRandomJoke(numberOfJokes = 1):
    if (numberOfJokes == 1):
        return random.choice(randomJokes)
    else:
        generatedJokeList = set(())
        while (len(generatedJokeList) < numberOfJokes):
            generatedJokeList.add(random.choice(randomJokes))
        return generatedJokeList
    
# print(getRandomJoke())
# print(getRandomJoke(2))
# print(getRandomJoke(20))

