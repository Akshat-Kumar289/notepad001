import pandas as pd
import os

def xlsx_to_csv(xlsx_file):
    xls = pd.ExcelFile(xlsx_file)
    output_folder = "generated_csv"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
        for column_name in df.columns:
            column_csv_file = os.path.join(output_folder, f"{column_name}.csv")
            column_df = pd.DataFrame(df[column_name])
            column_df.to_csv(column_csv_file, index=False)
            print(f"Converted {sheet_name}.{column_name} to {column_csv_file}")

if __name__ == '__main__':
    xlsx_file = r'C:\\myfiles\\flaskNotepad\\excelToCsv\\Financial_Sample.xlsx'
    xlsx_to_csv(xlsx_file)
