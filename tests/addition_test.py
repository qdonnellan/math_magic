import unittest
import json
import re 

from math_magic.generate_question import generate_question

class TestAdditionImplementation(unittest.TestCase):
    '''
    test class for the implementation of addition controllers
    '''

    def load_json_response(self, user_input):
        '''
        convenience handler to load json response from user input
        '''
        json_result = generate_question(user_input)
        return json.loads(json_result)

    def test_simple_non_random_example(self):
        '''
        test result of inputting a simple addition equation
        '''
        user_input = '2 + 4'
        data = self.load_json_response(user_input)
        self.assertEqual(data['answer'], '6')
        self.assertEqual(data['latex'], '\( 2 + 4 \)')

    def test_simple_random_example(self):
        '''
        test result of inputting a simple addition equation with random bits
        [1..10] + [1..10] should return something like 3 + 4 where 3 is a number
        between 0 and 10 inclusive, and 4 is as well
        '''
        user_input = '[0..10] + [0..10]'
        data = self.load_json_response(user_input)
        self.assertTrue(re.match('\d+.*+\d+', data['plain_text']))



