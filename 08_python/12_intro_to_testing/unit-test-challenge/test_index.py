import pytest   
from index import greetMessage, getRandomJoke
from randomJokesList import randomJokes      

# greetMessage - When given the input "Alex", the string returned is "Hello there, Alex!"
def test_greetMessage_Alex():
    assert greetMessage('Alex') == 'Hello there, Alex!'

# greetMessage - When given the input "300", the function throws an error
def getMessage_number():
    with pytest.raises(ValueError):
        assert greetMessage('300')

# greetMessage - When given no arguments, the function throws an error
def test_greetMessage_no_arguments():
    with pytest.raises(TypeError):
        greetMessage()

# getRandomJoke - When given no arguments, it returns a string that is found in the `randomJokes` variable. You may need to import this variable into your test code to complete this test.
def test_getRandomJoke_no_arguments():
    result = getRandomJoke()
    assert result in randomJokes

# getRandomJoke - When given a number as an argument, it returns a set of strings that contains no duplicates within the set and only contains content found in the `randomJokes`` variable.
def test_getRandomJoke_with_number():
    num_jokes = 3
    result = getRandomJoke(num_jokes)
    assert isinstance(result, set)
    assert len(result) == num_jokes
    assert all(joke in randomJokes for joke in result)
    assert len(set(result)) == len(result)


