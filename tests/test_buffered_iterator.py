import unittest

from buffered_iterator import BufferedIterator
from buffered_iterator import BufferedIteratorValueError
from buffered_iterator import BufferOverflowWarning


#%% Test Text
TEST_LINES = '''Line 0
Second Line
Third Line
Fourth Line
Fifth Line
~Line 6
Line 7
Line 8
Line 9
Line 10
Line 11
Line 12
'''
# from pprint import pprint
# pprint(TEST_LINES.splitlines())
#for i,l in enumerate(TEST_LINES.splitlines()):
#    print(f'{i}\t{l}')



#%%  Prescribed dose parse tests
class TestBufferedIterator(unittest.TestCase):
    def setUp(self):
        self.test_lines = TEST_LINES.splitlines()
        self.buffer_size = 5
        self.test_iter = BufferedIterator(self.test_lines,
                                         buffer_size=self.buffer_size)

    def test_backup(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Backup 2 lines
        self.test_iter.step_back = 2
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, yielded_lines[-2])

    def test_backup_error(self):
        # Step through 1st line
        yielded_lines = list()
        for i in range(1):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Try to Backup 2 lines
        with self.assertRaises(ValueError):
            self.test_iter.step_back = 2

    def test_backup_beyond_buffer_error(self):
        #  Step through more lines than buffer size
        yielded_lines = list()
        for i in range(self.buffer_size+1):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Try to Backup 2 lines
        with self.assertRaises(ValueError):
            self.test_iter.step_back = self.buffer_size+1

    def test_backup_method(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Backup 2 lines
        self.test_iter.backup(2)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, yielded_lines[-2])

    def test_look_back(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Backup 2 lines
        previous_line = self.test_iter.look_back(2)
        self.assertEqual(previous_line, yielded_lines[-2])
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, self.test_lines[3])

    def test_look_ahead(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Look 2 lines ahead
        future_line = self.test_iter.look_ahead(2)
        # Step through 2 more lines
        for i in range(2):
            yielded_lines.append(self.test_iter.__next__())
        self.assertEqual(future_line, yielded_lines[-1])

    def test_skip(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        previous_line = yielded_lines[-1]
        #Skip 3 lines ahead
        self.test_iter.skip(3)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, self.test_lines[3+3])
        #Backup 2 lines
        self.test_iter.backup(2)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, previous_line)


    def test_advance(self):
        # Step through 1st 3 lines
        yielded_lines = list()
        for i in range(3):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        previous_line = yielded_lines[-1]
        #Advance 3 lines ahead
        self.test_iter.advance(3)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, self.test_lines[3+3])
        #Backup 3+2 lines
        self.test_iter.backup(3+2)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, previous_line)

    def test_max_backup(self):
        # Advance to fill the buffer
        yielded_lines = list()
        for i in range(self.buffer_size):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        #Backup the entire buffer
        self.test_iter.backup(self.buffer_size)
        next_line = self.test_iter.__next__()
        self.assertEqual(next_line, yielded_lines[-self.buffer_size])

    def test_source_overun(self):
        # Advance to fill the buffer
        yielded_lines = list()
        num_items = len(self.test_lines)
        with self.assertRaises(StopIteration):
            for i in range(num_items+1):  # pylint: disable=unused-variable
                yielded_lines.append(self.test_iter.__next__())

    def test_advance_overun(self):
        # Advance to fill the buffer
        yielded_lines = list()
        num_items = len(self.test_lines)
        for i in range(num_items):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        with self.assertRaises(BufferOverflowWarning):
            self.test_iter.advance(1)

    def test_look_back_overun(self):
        # Advance to fill the buffer
        yielded_lines = list()
        for i in range(1):  # pylint: disable=unused-variable
            yielded_lines.append(self.test_iter.__next__())
        with self.assertRaises(BufferedIteratorValueError):
            previous_line = self.test_iter.look_back(2)  # pylint: disable=unused-variable


if __name__ == '__main__':
    unittest.main()

# %%
