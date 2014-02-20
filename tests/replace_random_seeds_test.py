import unittest
import json
import re 

from math_magic.replace_random_seeds import replace_random_seeds

class TestAdditionImplementation(unittest.TestCase):
    '''
    test class for the implementation of the random number seed replace function
    '''

    def test_single_random_number_with_varying_bounds(self):
        '''
        test result of inputting a simple random number in the set [a,b], (a,b), (a,b], and [a,b)

        repleat 1000 times to make sure the bounds are correct
        '''
        for user_input in ['[0..10)', '(0..10]', '(0..10)', '[0..10]']:
            for i in range(1000):
                output = int(replace_random_seeds(user_input))
                if '[' in user_input:  #square left-bracket means the lower bound is inclusive
                    self.assertGreaterEqual(output,0)
                else:
                    self.assertGreater(output, 0)

                if ']' in user_input: #square right-bracket means the upper bound is inclusive
                    self.assertLessEqual(output, 10)
                else:
                    self.assertLess(output, 10)

    def test_simple_addition_example(self):
        '''
        test result of inputting a simple addition equation with random number seeds 

        [1..10] + [1..10] should return something like 3 + 4 where 3 is a number
        between 0 and 10 inclusive, etc.
        '''
        user_input = '[0..10] + [0..10]'
        output = replace_random_seeds(user_input)
        self.assertTrue(re.match('(\d+).*[+].*(\d+)', output))

    def test_simple_sentence_with_random_number(self):
        '''
        test the replacement of a sentence with a random number seed 
        '''
        user_input = 'Hey, check out this random number: [20..30], it should be between 20 and 30'
        expected = re.compile('Hey, check out this random number: (\d+), it should be between 20 and 30')
        output = replace_random_seeds(user_input)
        self.assertTrue(re.match(expected, output))




