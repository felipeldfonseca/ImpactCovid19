#!/bin/bash

echo "🔬 CDC COVID-19 Data Analysis Setup"
echo "=================================="

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if packages are installed
echo "🔍 Checking dependencies..."
python -c "import pandas, jupyter, numpy, matplotlib, seaborn; print('✅ All packages available!')" || {
    echo "❌ Missing packages. Installing..."
    pip install -r requirements.txt
}

# Check if datasets are available
echo "📊 Checking datasets..."
python -c "
import os
import pandas as pd
base_path = 'Datasets/Impact of Covid-19 in different countries/CDC'
datasets = [
    'Cases by Age Group/cases_by_age_group.csv',
    'Cases by Race:Ethnicity/cases_by_race_ethnicity__all_age_groups.csv',
    'Cases by Sex/cases_by_sex__all_age_groups.csv',
    'Deaths by Age Group/deaths_by_age_group.csv',
    'Deaths by Race:Ethnicity/deaths_by_race_ethnicity__all_age_groups.csv',
    'Deaths by Sex/deaths_by_sex__all_age_groups.csv'
]
missing = []
for dataset in datasets:
    if not os.path.exists(os.path.join(base_path, dataset)):
        missing.append(dataset)

if missing:
    print(f'❌ Missing datasets: {missing}')
    exit(1)
else:
    print('✅ All CDC datasets found!')
"

if [ $? -ne 0 ]; then
    echo "❌ Dataset check failed. Please ensure all CDC datasets are in the correct locations."
    exit 1
fi

echo ""
echo "🚀 All checks passed! Launching Jupyter Notebook..."
echo "📝 Open 'ImpactCovid19_CDC_Only.ipynb' in your browser"
echo ""
echo "💡 Remember to select the correct Python kernel if prompted!"
echo ""

# Launch Jupyter Notebook
jupyter notebook 