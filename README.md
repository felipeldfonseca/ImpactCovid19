# Impact COVID-19 - CDC Analysis Project

A comprehensive data analysis project focusing on CDC COVID-19 datasets, examining cases and deaths across different demographic groups (age, race/ethnicity, and sex).

## 📊 Project Overview

This project analyzes COVID-19 impact using official CDC datasets to understand patterns and trends across different demographic segments. The analysis includes data cleaning, transformation, and visualization, with exports ready for Business Intelligence tools.

### Key Features
- **6 CDC Dataset Analysis**: Cases and Deaths by Age Groups, Race/Ethnicity, and Sex
- **Data Quality Processing**: Handles range values, special characters, and missing data
- **Interactive Visualizations**: Charts and graphs using matplotlib, seaborn, and plotly
- **BI Tool Exports**: Clean CSV files ready for Power BI, Tableau, and Looker Studio
- **Robust Error Handling**: Multiple fallback methods for data export

## 🏗️ Project Structure

```
ImpactCovid19/
├── ImpactCovid19_CDC_Only.ipynb    # Main analysis notebook
├── requirements.txt                 # Python dependencies
├── README_Setup.md                 # Detailed setup instructions
├── launch_notebook.sh              # Quick launch script
├── data_cleaning_cell.py           # Data cleaning utilities
├── export_cleaned_data.py          # Basic export script
├── robust_export_solution.py       # Advanced export with fallbacks
├── Datasets/                       # CDC data files (not in repo)
│   ├── CDC_Cases_by_Age_Group.csv
│   ├── CDC_Deaths_by_Age_Group.csv
│   ├── CDC_Cases_by_Race_Ethnicity.csv
│   ├── CDC_Deaths_by_Race_Ethnicity.csv
│   ├── CDC_Cases_by_Sex.csv
│   └── CDC_Deaths_by_Sex.csv
└── clean_cdc_datasets/            # Processed exports (generated)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- Virtual environment support

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ImpactCovid19.git
   cd ImpactCovid19
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv venv_fixed
   source venv_fixed/bin/activate  # On Windows: venv_fixed\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add CDC datasets**: Place your CDC COVID-19 CSV files in the `Datasets/` folder

5. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

### Quick Launch (Alternative)
```bash
chmod +x launch_notebook.sh
./launch_notebook.sh
```

## 📈 Usage

### Running the Analysis
1. Open `ImpactCovid19_CDC_Only.ipynb` in Jupyter
2. Run all cells to perform the complete analysis
3. View generated visualizations and insights

### Exporting Clean Data
After running the notebook, export cleaned datasets for BI tools:

```bash
python3 robust_export_solution.py
```

This creates clean CSV files in `clean_cdc_datasets/` folder, ready for:
- **Power BI**: Get Data → Text/CSV
- **Tableau**: Connect → Text File  
- **Looker Studio**: Upload CSV files
- **Excel**: Open CSV files directly

## 🧹 Data Cleaning Features

The project handles various data quality issues:

- **Range Values**: Converts "436120 - 436129" to midpoint (436124.5)
- **Special Characters**: Transforms "<0.1" to numeric (0.05)
- **Missing Data**: Standardizes "N/A" values to NaN
- **Column Standardization**: Ensures consistent naming across datasets
- **Data Type Conversion**: Proper numeric and date formatting

## 📊 Analysis Sections

The notebook includes 17 comprehensive analysis sections:

1. **Data Loading & Overview**
2. **Age Group Analysis** (Cases & Deaths)
3. **Race/Ethnicity Analysis** (Cases & Deaths)  
4. **Sex-based Analysis** (Cases & Deaths)
5. **Comparative Demographics**
6. **Trend Analysis**
7. **Statistical Summaries**
8. **Correlation Analysis**
9. **Data Quality Assessment**
10. **Missing Data Analysis**
11. **Outlier Detection**
12. **Demographic Cross-Analysis**
13. **Rate Calculations**
14. **Seasonal Patterns**
15. **Geographic Insights**
16. **Risk Factor Analysis**
17. **Summary & Recommendations**

## 🛠️ Dependencies

Key Python packages:
- `pandas` - Data manipulation and analysis
- `jupyter` - Interactive notebook environment
- `numpy` - Numerical computing
- `matplotlib` - Static visualizations
- `seaborn` - Statistical visualizations
- `plotly` - Interactive charts
- `openpyxl` - Excel file support

See `requirements.txt` for complete list with versions.

## 🔧 Troubleshooting

### Common Issues

**Virtual Environment Problems**:
```bash
# Create fresh environment
python3 -m venv venv_fixed
source venv_fixed/bin/activate
pip install -r requirements.txt
```

**Pandas Import Errors**:
```bash
# Reinstall pandas
pip uninstall pandas
pip install pandas==2.1.4
```

**Export Issues**: Use `robust_export_solution.py` which includes multiple fallback methods.

## 📊 Data Sources

This project uses official CDC COVID-19 datasets:
- CDC Cases and Deaths by Age Group
- CDC Cases and Deaths by Race and Hispanic Origin
- CDC Cases and Deaths by Sex

*Note: Dataset files are not included in the repository due to size. Download from official CDC sources.*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new analysis'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- CDC for providing comprehensive COVID-19 datasets
- Python community for excellent data analysis libraries
- Contributors and users of this analysis tool

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue or contact the maintainer.

---
**Last Updated**: June 2025 
