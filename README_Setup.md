# CDC COVID-19 Data Analysis - Setup Guide

## Overview
This project analyzes CDC COVID-19 datasets to understand the impact of the pandemic across different demographics in the United States, including analysis by age groups, race/ethnicity, and sex.

## Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab

## Setup Instructions

### 1. Activate Virtual Environment
The project has a virtual environment set up. Activate it:

```bash
# On macOS/Linux
source venv/bin/activate

# On Windows (if recreating the environment)
venv\Scripts\activate
```

### 2. Install Dependencies (Already Done!)
The required packages have been installed. If you need to reinstall them:

```bash
pip install -r requirements.txt
```

### 3. Verify Dataset Structure
Ensure your datasets are organized as follows:
```
Datasets/
└── Impact of Covid-19 in different countries/
    └── CDC/
        ├── Cases by Age Group/
        │   └── cases_by_age_group.csv
        ├── Cases by Race:Ethnicity/
        │   └── cases_by_race_ethnicity__all_age_groups.csv
        ├── Cases by Sex/
        │   └── cases_by_sex__all_age_groups.csv
        ├── Deaths by Age Group/
        │   └── deaths_by_age_group.csv
        ├── Deaths by Race:Ethnicity/
        │   └── deaths_by_race_ethnicity__all_age_groups.csv
        └── Deaths by Sex/
            └── deaths_by_sex__all_age_groups.csv
```

### 4. Launch Jupyter Notebook
Start Jupyter Notebook with the virtual environment activated:

```bash
source venv/bin/activate
jupyter notebook
```

### 5. Open the Analysis Notebook
Open `ImpactCovid19_CDC_Only.ipynb` in your Jupyter interface.

### 6. Select the Correct Kernel
In Jupyter Notebook:
1. Go to `Kernel` → `Change Kernel`
2. Select `Python 3 (ipykernel)` which should correspond to your `venv` environment
3. If the kernel isn't available, install it with:
   ```bash
   source venv/bin/activate
   python -m ipykernel install --user --name=venv --display-name="Python 3 (CDC Analysis)"
   ```

## Available Datasets

The notebook analyzes six CDC datasets:

1. **Cases by Age Group** - COVID-19 cases distributed across different age ranges
2. **Cases by Race/Ethnicity** - COVID-19 cases by racial and ethnic demographics
3. **Cases by Sex** - COVID-19 cases by gender
4. **Deaths by Age Group** - COVID-19 deaths distributed across different age ranges
5. **Deaths by Race/Ethnicity** - COVID-19 deaths by racial and ethnic demographics
6. **Deaths by Sex** - COVID-19 deaths by gender

## Key Analysis Features

- **Data Quality Assessment** - Check for missing values and data integrity
- **Demographic Analysis** - Compare impact across different population groups
- **Statistical Summary** - Key metrics and trends from CDC data
- **Clean Data Processing** - Proper handling of data types and formats

## Environment Status ✅

- ✅ Virtual environment created (`venv`)
- ✅ All dependencies installed
- ✅ Clean notebook created (`ImpactCovid19_CDC_Only.ipynb`)
- ✅ Dataset structure verified
- ✅ Ready to run!

## Quick Start Commands

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Start Jupyter
jupyter notebook

# 3. Open ImpactCovid19_CDC_Only.ipynb
# 4. Run all cells to see the analysis
```

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure the virtual environment is activated and dependencies are installed
2. **File Path Errors**: Verify that the dataset directory structure matches the expected layout
3. **Kernel Issues**: Make sure you've selected the correct Python kernel

### Setting up a Custom Kernel (if needed):
```bash
source venv_new/bin/activate
python -m ipykernel install --user --name=cdc_analysis --display-name="Python 3 (CDC Analysis)"
```

## Dependencies
- pandas: Data manipulation and analysis
- jupyter: Notebook interface
- ipython: Enhanced Python shell
- numpy: Numerical computing
- matplotlib: Plotting library
- seaborn: Statistical data visualization
- plotly: Interactive visualizations
- openpyxl & xlrd: Excel file support

## Next Steps
The notebook is set up for comprehensive data exploration. You can extend it by adding:
- Data visualizations (charts, graphs)
- Statistical analysis
- Comparative studies
- Trend analysis over time
- Correlation analysis between demographics

## Support
If you encounter any issues, check that:
1. Virtual environment (`venv_new`) is activated
2. All dependencies are installed
3. Dataset files are in the correct locations
4. Jupyter is running in the project directory
5. Correct kernel is selected in Jupyter 