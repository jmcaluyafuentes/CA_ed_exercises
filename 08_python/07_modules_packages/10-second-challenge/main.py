import time

def compute_time():
    print('10 Second Challenge')
    input('Press Enter to start the challenge.')
    first_time = time.time()
    input('Press Enter again to end the time.')
    second_time = time.time()
    time_difference = second_time - first_time

    compare_time = 10 - time_difference
    if compare_time == 0:
        print('You hit the 10 seconds mark')
    elif compare_time > 0:
        print('You\'re time is less than 10 seconds')
    else:
        print('You\'re time is more than 10 seconds')

compute_time()
