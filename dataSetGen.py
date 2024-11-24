import pandas as pd
import numpy as np
from faker import Faker

# Generate synthetic data
faker = Faker()
np.random.seed(42)

# Create a dataset
data = {
    "Name": [faker.name() for _ in range(200000)],
    "Age": np.random.randint(22, 60, 200000),
    "Years_of_Experience": np.random.randint(0, 40, 200000),
    "Current_Salary": np.random.randint(20000, 200000, 200000),
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("hr_salary_data.csv", index=False)
print("Synthetic dataset generated and saved!")

