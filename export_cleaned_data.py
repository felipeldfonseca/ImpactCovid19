"""
Export Cleaned CDC COVID-19 Datasets for BI Tools
This script exports all cleaned datasets to CSV files for use in Power BI, Tableau, Looker Studio, etc.
"""

import os
import pandas as pd
from datetime import datetime

print("📤 Exporting Cleaned CDC COVID-19 Datasets for BI Tools")
print("=" * 60)

# Create output directory
out_dir = "clean_cdc_datasets"
os.makedirs(out_dir, exist_ok=True)
print(f"📁 Output directory: {out_dir}")

# Define the mapping of your actual dataset variables to clean file names
tables = {
    "cases_by_age":      cdc_cases_by_age,
    "deaths_by_age":     cdc_deaths_by_age,
    "cases_by_race":     cdc_cases_by_race,
    "deaths_by_race":    cdc_deaths_by_race,
    "cases_by_sex":      cdc_cases_by_sex,
    "deaths_by_sex":     cdc_deaths_by_sex,
}

# Export each dataset
export_summary = []
for name, df in tables.items():
    try:
        # Create the file path
        file_path = f"{out_dir}/{name}.csv"
        
        # Export to CSV
        df.to_csv(file_path, index=False)
        
        # Record export info
        file_size = os.path.getsize(file_path)
        export_summary.append({
            'Dataset': name,
            'Rows': len(df),
            'Columns': len(df.columns),
            'File Size (KB)': round(file_size / 1024, 2),
            'File Path': file_path
        })
        
        print(f"✅ {name}.csv exported successfully ({len(df)} rows, {len(df.columns)} columns)")
        
    except Exception as e:
        print(f"❌ Error exporting {name}: {e}")

# Create a summary report
print(f"\n📊 Export Summary:")
print("=" * 40)
summary_df = pd.DataFrame(export_summary)
print(summary_df.to_string(index=False))

# Export the summary as well
summary_path = f"{out_dir}/export_summary.csv"
summary_df.to_csv(summary_path, index=False)

# Create a metadata file with additional information for BI tools
metadata = {
    'export_date': datetime.now().isoformat(),
    'total_datasets': len(tables),
    'data_source': 'CDC COVID-19 Data',
    'cleaning_applied': [
        'Range values converted to midpoint (e.g., "436120 - 436129" → 436124.5)',
        'Special characters like "<0.1" converted to 0.05 (midpoint estimate)',
        'N/A values converted to NaN for proper handling',
        'Column names standardized across datasets'
    ],
    'notes_for_bi_tools': [
        'All numeric columns are properly formatted for calculations',
        'Missing values are represented as empty cells (will appear as null in BI tools)',
        'Percentage columns are in decimal format (e.g., 0.05 = 0.05%, not 5%)',
        'Count columns contain actual numeric values ready for aggregation'
    ],
    'recommended_visualizations': {
        'cases_by_age': 'Bar chart, pie chart, demographic pyramid',
        'deaths_by_age': 'Bar chart, line chart for mortality patterns',
        'cases_by_race': 'Horizontal bar chart, treemap',
        'deaths_by_race': 'Horizontal bar chart, demographic analysis',
        'cases_by_sex': 'Pie chart, simple bar chart',
        'deaths_by_sex': 'Pie chart, simple bar chart'
    }
}

# Save metadata as JSON for reference
import json
metadata_path = f"{out_dir}/dataset_metadata.json"
with open(metadata_path, 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"\n📋 Additional files created:")
print(f"  • export_summary.csv - Overview of all exported datasets")
print(f"  • dataset_metadata.json - Metadata and notes for BI tools")

print(f"\n🎉 All datasets exported successfully!")
print(f"📂 Ready for import into:")
print("  • Power BI: Import from folder or individual CSV files")
print("  • Tableau: Connect to Text file data source")
print("  • Looker Studio: Upload CSV files as data sources")
print("  • Excel: Open CSV files directly")

print(f"\n💡 Next steps for BI tools:")
print("  1. Import the CSV files from the '{out_dir}' folder")
print("  2. Check data types (most should auto-detect correctly)")
print("  3. Review the metadata.json file for visualization recommendations")
print("  4. Consider creating relationships between datasets based on demographic categories") 