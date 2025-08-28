# Dataframe Data

import pandas as pd

# Data
# Add Real Values
sampleData = {
    "Name": ["Sunil Pillai", "Gaurav Sharma", "Karthik Thakur"],
    "ODI": [100, 120,130],
    "Test": [200, 220,230]
}

# Create DataFrame
df = pd.DataFrame(sampleData)

# Print DataFrame
print(df)