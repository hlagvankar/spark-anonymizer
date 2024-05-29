
### Step 6: Testing
"""
Create unit tests to verify the anonymization process.

**tests/test_anonymize_data.py:**

"""
import unittest
import pandas as pd
from src.anonymize_data import anonymize_data
import os

class TestAnonymizeData(unittest.TestCase):

    def setUp(self):
        self.input_file = 'data/input_test.csv'
        self.output_file = 'data/output_test.csv'
        data = {
            "first_name": ["John", "Jane"],
            "last_name": ["Doe", "Smith"],
            "address": ["123 Main St", "456 Elm St"],
            "date_of_birth": ["1980-01-01", "1990-02-02"],
        }
        df = pd.DataFrame(data)
        df.to_csv(self.input_file, index=False)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_anonymize_data(self):
        anonymize_data(self.input_file, self.output_file)
        df_anonymized = pd.read_csv(self.output_file)
        self.assertFalse(df_anonymized['first_name'].str.contains("John|Jane").any())
        self.assertFalse(df_anonymized['last_name'].str.contains("Doe|Smith").any())
        self.assertFalse(df_anonymized['address'].str.contains("123 Main St|456 Elm St").any())

if __name__ == '__main__':
    unittest.main()
