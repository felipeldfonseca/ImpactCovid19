"""
Robust Export Solution for CDC COVID-19 Datasets
This script provides multiple methods to export data when pandas.to_csv() fails
"""

import os
import csv
import json
from datetime import datetime

print("📤 Robust Export for CDC COVID-19 Datasets")
print("=" * 50)

# Create output directory
out_dir = "clean_cdc_datasets"
os.makedirs(out_dir, exist_ok=True)
print(f"📁 Output directory: {out_dir}")

# Define datasets to export
datasets = {
    "cases_by_age": cdc_cases_by_age,
    "deaths_by_age": cdc_deaths_by_age,
    "cases_by_race": cdc_cases_by_race,
    "deaths_by_race": cdc_deaths_by_race,
    "cases_by_sex": cdc_cases_by_sex,
    "deaths_by_sex": cdc_deaths_by_sex,
}

def export_with_csv_module(df, filepath):
    """Export using Python's built-in csv module (more reliable)"""
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(df.columns.tolist())
            
            # Write data rows
            for _, row in df.iterrows():
                # Convert any NaN values to empty strings
                clean_row = []
                for value in row:
                    if pd.isna(value):
                        clean_row.append('')
                    else:
                        clean_row.append(str(value))
                writer.writerow(clean_row)
        return True
    except Exception as e:
        print(f"❌ CSV module export failed: {e}")
        return False

def export_with_manual_write(df, filepath):
    """Manual CSV export as backup method"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write header
            f.write(','.join(df.columns) + '\n')
            
            # Write data
            for _, row in df.iterrows():
                clean_values = []
                for value in row:
                    if pd.isna(value):
                        clean_values.append('')
                    else:
                        # Escape commas and quotes in data
                        str_value = str(value)
                        if ',' in str_value or '"' in str_value:
                            str_value = f'"{str_value.replace('"', '""')}"'
                        clean_values.append(str_value)
                f.write(','.join(clean_values) + '\n')
        return True
    except Exception as e:
        print(f"❌ Manual export failed: {e}")
        return False

# Export each dataset with multiple fallback methods
export_summary = []
successful_exports = 0

for name, df in datasets.items():
    print(f"\n🔄 Exporting {name}...")
    filepath = f"{out_dir}/{name}.csv"
    
    # Method 1: Try pandas to_csv (might fail)
    success = False
    try:
        df.to_csv(filepath, index=False)
        print(f"✅ Method 1 (pandas) succeeded for {name}")
        success = True
    except Exception as e:
        print(f"⚠️  Method 1 (pandas) failed: {str(e)[:50]}...")
        
        # Method 2: Try Python's csv module
        if export_with_csv_module(df, filepath):
            print(f"✅ Method 2 (csv module) succeeded for {name}")
            success = True
        else:
            # Method 3: Manual write
            if export_with_manual_write(df, filepath):
                print(f"✅ Method 3 (manual) succeeded for {name}")
                success = True
    
    if success:
        # Record export info
        file_size = os.path.getsize(filepath)
        export_summary.append({
            'Dataset': name,
            'Rows': len(df),
            'Columns': len(df.columns),
            'File Size (KB)': round(file_size / 1024, 2),
            'Status': 'Success'
        })
        successful_exports += 1
        print(f"📄 {name}.csv: {len(df)} rows, {len(df.columns)} columns, {file_size/1024:.1f}KB")
    else:
        export_summary.append({
            'Dataset': name,
            'Rows': len(df),
            'Columns': len(df.columns),
            'File Size (KB)': 0,
            'Status': 'Failed'
        })
        print(f"❌ Failed to export {name}")

# Create summary report
print(f"\n📊 Export Summary:")
print("=" * 50)
print(f"Total datasets: {len(datasets)}")
print(f"Successful exports: {successful_exports}")
print(f"Failed exports: {len(datasets) - successful_exports}")

# Display detailed summary
print(f"\nDetailed Summary:")
for item in export_summary:
    status_icon = "✅" if item['Status'] == 'Success' else "❌"
    print(f"{status_icon} {item['Dataset']}: {item['Rows']} rows, {item['Columns']} cols, {item['File Size (KB)']}KB")

# Create a simple summary file
summary_content = "Dataset,Rows,Columns,File_Size_KB,Status\n"
for item in export_summary:
    summary_content += f"{item['Dataset']},{item['Rows']},{item['Columns']},{item['File Size (KB)']},{item['Status']}\n"

with open(f"{out_dir}/export_summary.csv", 'w') as f:
    f.write(summary_content)

print(f"\n🎉 Export completed!")
if successful_exports == len(datasets):
    print("✅ All datasets exported successfully!")
else:
    print(f"⚠️  {len(datasets) - successful_exports} datasets failed to export")

print(f"\n📂 Files available in '{out_dir}' folder:")
try:
    files = os.listdir(out_dir)
    for file in sorted(files):
        if file.endswith('.csv'):
            size = os.path.getsize(f"{out_dir}/{file}")
            print(f"  • {file} ({size/1024:.1f}KB)")
except Exception as e:
    print(f"Error listing files: {e}")

if successful_exports > 0:
    print(f"\n💡 Your datasets are ready for BI tools!")
    print("📥 Import instructions:")
    print("  • Power BI: Get Data → Text/CSV")
    print("  • Tableau: Connect → Text File")
    print("  • Looker Studio: Upload CSV files")
    print("  • Excel: Open CSV files directly") 