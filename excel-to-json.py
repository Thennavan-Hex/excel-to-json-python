import pandas as pd

def excel_to_json(excel_file_path, json_file_path):
    df = pd.read_excel(excel_file_path)
    df.to_json(json_file_path, orient='records')


excel_file_path = 'itb2.xlsx'  # Replace with the path to your Excel file
json_file_path = 'output.json'  # Replace with the desired output JSON file path

excel_to_json(excel_file_path, json_file_path)

