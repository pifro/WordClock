import unittest
import wordclock

class wordClockTest(unittest.TestCase):

    def testReproduce(self):
        start = [
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 1]
        ]
        expected = [
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 1],
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 1],
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 1],
        ]
        result = wordclock.reproducePopulation(start, 6)
        self.assertListEqual(result, expected)

    def testCull(self):
        start = [
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 2],
            [['Tata', 'Tutu'], 4],
            [['Tata', 'Tutu'], 5]
        ]
        expected = [
            [['Toto', 'Titi'], 1],
            [['Tata', 'Tutu'], 2],
        ]
        result = wordclock.cullPopulation(start, 2)
        self.assertListEqual(result, expected)


if __name__ == '__main__' :
    unittest.main()