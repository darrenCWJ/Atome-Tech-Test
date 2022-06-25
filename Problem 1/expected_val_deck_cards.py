"""
There is a deck of 54 cards, all facing down. Given a series of integers 𝑥0, 𝑥1, 𝑥2, … , 𝑥𝑛−1, 
we are going to conduct the following random experiment:
For each 𝑥𝑖 :
1) pick the first 𝑥𝑖 cards and turn them over;
2) completely shuffle all the cards by random.
Let 𝑈 denote the number of cards that are facing up by the end of the experiment. Due 
to the randomness of the experiment, we don't always end up with the same 𝑈. Can you 
implement a function that calculates the expected value of 𝑈? (Don't use random library; 
simulation is not required.)

Input:
A list of integers 𝑥, each integer 𝑥𝑖 between 0 and 54, inclusive.
Return:
A single float of the expected number of face-up cards.

Example:
Input: x = [1]
Return: 1.0
Input: x = [27, 1]
Return: 27.0


# expected value calculation: E(x) = p(x) * x
"""

def facing_up(x):
    chance_face_up = 0.
    chance_face_down = 1.
    expected_val = 0.
    for i in x:
        normalise_val = i/54
        expected_val += (normalise_val * chance_face_down) - (normalise_val * chance_face_up)
        chance_face_down = 1. - expected_val
        chance_face_up = expected_val
    return expected_val * 54



if __name__ == "__main__":
    x = [27, 1]
    print(f'Expected face up cards {facing_up(x)}')