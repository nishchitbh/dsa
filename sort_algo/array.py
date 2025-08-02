import random


def generate_array(size):
    generated = list(range(size))
    random.shuffle(generated)
    return generated
