import unittest
from file_parser import map_protocol, lookup_table, log_mapping

class test_file_parser(unittest.TestCase):
    # test case one to check if the map protocol works as we thought
    def test_map_protocol_known(self):
        self.assertEqual(map_protocol(6), "tcp")

    # Check if the function is extracting tags properly
    # Checks if it returns "sv_P1"
    def test_lookup_table(self):
        self.assertEqual(lookup_table(25, "tcp", 'lookup_table.csv'), "sv_P1")
    # Checks if it returns "Untagged"
    def test_lookup_table_not_found(self):
        self.assertEqual(lookup_table(1, "HTTP", 'lookup_table.csv'), "Untagged")

    ## Now doing testing if it is generating the output properly and we are getting the expected output
    def test_log_mapping_output(self):
        with open('test.txt', 'r') as f:
            count_tags, port_protocol_count = log_mapping('test.txt', 'tagged_output.txt')
            self.assertTrue('sv_P1' in count_tags)
            self.assertTrue((80, 'tcp') in port_protocol_count)

if __name__ == '__main__':
    unittest.main()