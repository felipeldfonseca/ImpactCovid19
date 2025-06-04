"""
CDC COVID-19 Data Cleaning and Transformation
This cell cleans all the data quality issues identified in the CDC datasets.
"""

import pandas as pd
import numpy as np

print("🧹 Starting CDC Data Cleaning Process...")
print("=" * 50)

# Function to convert range values to numeric (for Deaths by Sex dataset)
def convert_range_to_numeric(value):
    """Convert range values like '436120 - 436129' to midpoint"""
    if isinstance(value, str) and ' - ' in value:
        try:
            start, end = value.split(' - ')
            return (int(start) + int(end)) / 2
        except ValueError:
            return np.nan
    return value

# Function to handle special characters like "<0.1"
def convert_less_than(value):
    """Convert '<0.1' to 0.05 (midpoint estimate)"""
    if isinstance(value, str) and value.startswith('<'):
        try:
            return float(value[1:]) / 2
        except ValueError:
            return np.nan
    return value

# Function to clean percentage columns
def clean_percentage_column(series):
    """Clean percentage columns that may contain '<' symbols"""
    return series.apply(convert_less_than)

# Function to clean count columns
def clean_count_column(series):
    """Clean count columns that may contain ranges or special characters"""
    return series.apply(convert_range_to_numeric)

print("🔧 Cleaning Cases by Sex dataset...")
# Clean Cases by Sex
if 'cdc_cases_by_sex' in locals():
    # Handle '<0.1' in Percent of cases
    cdc_cases_by_sex['Percent of cases'] = clean_percentage_column(cdc_cases_by_sex['Percent of cases'])
    # Replace 'N/A' with NaN
    cdc_cases_by_sex = cdc_cases_by_sex.replace('N/A', np.nan)
    print("✅ Cases by Sex cleaned")
else:
    print("⚠️  cdc_cases_by_sex not found - make sure datasets are loaded first")

print("🔧 Cleaning Deaths by Sex dataset...")
# Clean Deaths by Sex (most problematic dataset)
if 'cdc_deaths_by_sex' in locals():
    # Handle range values in Count of deaths
    cdc_deaths_by_sex['Count of deaths'] = clean_count_column(cdc_deaths_by_sex['Count of deaths'])
    # Handle '<0.1' in Percentage of deaths
    cdc_deaths_by_sex['Percentage of deaths'] = clean_percentage_column(cdc_deaths_by_sex['Percentage of deaths'])
    # Replace 'N/A' with NaN
    cdc_deaths_by_sex = cdc_deaths_by_sex.replace('N/A', np.nan)
    # Standardize column name
    cdc_deaths_by_sex = cdc_deaths_by_sex.rename(columns={'Percentage of deaths': 'Percent of deaths'})
    print("✅ Deaths by Sex cleaned")
else:
    print("⚠️  cdc_deaths_by_sex not found")

print("🔧 Cleaning Deaths by Age dataset...")
# Clean Deaths by Age
if 'cdc_deaths_by_age' in locals():
    # Handle '<0.1' in Percentage of deaths
    cdc_deaths_by_age['Percentage of deaths'] = clean_percentage_column(cdc_deaths_by_age['Percentage of deaths'])
    # Standardize column name
    cdc_deaths_by_age = cdc_deaths_by_age.rename(columns={'Percentage of deaths': 'Percent of deaths'})
    print("✅ Deaths by Age cleaned")
else:
    print("⚠️  cdc_deaths_by_age not found")

print("🔧 Cleaning Deaths by Race/Ethnicity dataset...")
# Clean Deaths by Race/Ethnicity
if 'cdc_deaths_by_race' in locals():
    # Standardize column name
    cdc_deaths_by_race = cdc_deaths_by_race.rename(columns={'Percentage of deaths': 'Percent of deaths'})
    print("✅ Deaths by Race/Ethnicity cleaned")
else:
    print("⚠️  cdc_deaths_by_race not found")

# Verify data types after cleaning
print("\n📊 Data Validation After Cleaning:")
print("=" * 40)

datasets_to_check = [
    ('Cases by Age', 'cdc_cases_by_age'),
    ('Cases by Race', 'cdc_cases_by_race'),
    ('Cases by Sex', 'cdc_cases_by_sex'),
    ('Deaths by Age', 'cdc_deaths_by_age'),
    ('Deaths by Race', 'cdc_deaths_by_race'),
    ('Deaths by Sex', 'cdc_deaths_by_sex')
]

for name, var_name in datasets_to_check:
    if var_name in locals():
        df = locals()[var_name]
        print(f"\n{name}:")
        print(f"  Shape: {df.shape}")
        print(f"  Missing values: {df.isnull().sum().sum()}")
        
        # Check numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print(f"  Numeric columns: {list(numeric_cols)}")
        
        # Check for any remaining problematic values
        for col in df.columns:
            if df[col].dtype == 'object':
                unique_vals = df[col].unique()
                problematic = [v for v in unique_vals if isinstance(v, str) and ('<' in str(v) or ' - ' in str(v) or v == 'N/A')]
                if problematic:
                    print(f"  ⚠️  Still problematic in {col}: {problematic}")

print("\n✅ Data cleaning completed!")
print("📈 Your datasets are now ready for visualization and analysis.")
print("\n💡 Notes:")
print("  - '<0.1' values converted to 0.05 (midpoint estimate)")
print("  - Range values converted to midpoint (e.g., '436120 - 436129' → 436124.5)")
print("  - 'N/A' values converted to NaN for proper handling")
print("  - Column names standardized across datasets") 