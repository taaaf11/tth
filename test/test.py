import unittest

from src.tth import Column


class TestColumn(unittest.TestCase):
    def setUp(self):
        self.A = Column(1, 3)
        self.B = Column(2, 3, first_col=self.A)
        self.C = Column(3, 3, first_col=self.A)
        
        self.A_col = ['A', *[0] * 4, *[1] * 4]
        self.B_col = ['B', *[0, 0, 1, 1] * 2]
        self.C_col = ['C', *[0, 1] * 4]
        
        self.input_cols = [self.A_col, self.B_col, self.C_col]
    
    # test for input variables
    def test_init(self):
        confirmation = [
            *self.input_cols
        ]
        
        self.assertTrue(self.A.table == confirmation)
    
    def test_and(self):
        self.A & self.B

        resultant_column = [r'A \cdot B', *[0] * 6, 1, 1]
        confirmation = [
            *self.input_cols,
            resultant_column
        ]
        self.assertTrue(self.A.table == confirmation)

        self.A * self.B
        confirmation = [
            *self.input_cols,
            resultant_column,
            resultant_column
        ]
        self.assertTrue(self.A.table == confirmation)
    
    def test_or(self):
        self.A | self.B
        resultant_column = ['A + B', 0, 0, *[1] * 6]

        confirmation = [
            *self.input_cols,
            resultant_column
        ]
        self.assertTrue(self.A.table == confirmation)

        self.A + self.B
        confirmation = [
            *self.input_cols,
            resultant_column,
            resultant_column
        ]
        self.assertTrue(self.A.table == confirmation)
        
    def test_not(self):
        ~(self.A)
        resultant_column = [r'\overline{A}', *[1] * 4, *[0] * 4]

        confirmation = [
            *self.input_cols,
            resultant_column
        ]
        
        self.assertTrue(self.A.table == confirmation)
        
    def test_grand_test(self):
        A = self.A
        B = self.B
        C = self.C
        
        exp_one = A & B & C
        
        confirmation_table = [
            *self.input_cols,
            [r'A \cdot B', *([0] * 6), 1, 1],
            [r'A \cdot B \cdot C', *([0] * 7), 1],
        ]
        
        exp_two = A & ~B
        
        confirmation_table += [
            [r'\overline{B}', *([1, 1, 0, 0] * 2)],
            [r'A \cdot \overline{B}', *([0] * 4), 1, 1, 0, 0]
        ]
        
        exp_three = ~(~A & ~C)
        
        confirmation_table += [
            [r'\overline{A}', *[1] * 4, *[0] * 4],
            [r'\overline{C}', *[1, 0] * 4],
            [r'\overline{A} \cdot \overline{C}', 1, 0, 1, *[0] * 5],
            [r'\overline{\overline{A} \cdot \overline{C}}', 0, 1, 0, *[1] * 5]
        ]
        
        final_exp = exp_one + exp_two + exp_three
        confirmation_table += [
            [r'A \cdot B \cdot C + A \cdot \overline{B}', *[0] * 4, 1, 1, 0, 1],
            [r'A \cdot B \cdot C + A \cdot \overline{B} + \overline{\overline{A} \cdot \overline{C}}',
             0, 1, 0, *[1] * 5
            ]
        ]
        
        self.assertTrue(A.table, confirmation_table)
    
    
if __name__ == '__main__':
    unittest.main()