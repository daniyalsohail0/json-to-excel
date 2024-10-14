import json
import pandas as pd

# Function to convert JSON to Excel
def convert_json_to_excel(json_file, output_excel):
    # Read the large JSON file with utf-8-sig to handle BOM
    with open(json_file, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Export the DataFrame to an Excel file
    df.to_excel(output_excel, index=False, engine='xlsxwriter')

    print(f"Excel file '{output_excel}' created successfully!")

# Main function
if __name__ == "__main__":
    input_json = 'charity.json'  # Path to your large JSON file
    output_excel = 'charities.xlsx'  # Output Excel file name

    convert_json_to_excel(input_json, output_excel)
