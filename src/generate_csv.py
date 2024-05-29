import pandas as pd
import faker
import sys

def generate_csv(file_path, num_of_rec):
    fake = faker.Faker()
    data = {
        "first_name": [fake.first_name() for _ in range(num_of_rec)],
        "last_name": [fake.last_name() for _ in range(num_of_rec)],
        "address": [fake.address() for _ in range(num_of_rec)],
        "date_of_birth": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_of_rec)],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    number_of_rec = sys.argv[1] if len(sys.argv) > 1 else 100
    generate_csv('../data/input.csv', number_of_rec)