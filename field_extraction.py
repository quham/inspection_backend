import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

def extract_field_tx_6_items(file_path):
    """
    Extract text from items with name 'Field_Tx_6_{number}' in a DXL file.
    
    Args:
        file_path: Path to the DXL file
    
    Returns:
        Dictionary with item names as keys and their text content as values
    """
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Since DXL files might not be well-formed XML, use regex to extract items
    pattern = r'<item\s+name=[\'"]Field_Tx_6_(\d+)[\'"]>\s*<text>(.*?)</text>\s*</item>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    results = {}
    for number, text in matches:
        item_name = f'Field_Tx_6_{number}'
        # Clean up the text - replace <break/> with newlines and remove extra whitespace
        clean_text = re.sub(r'<break\s*/>', '\n', text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        results[item_name] = clean_text
    
    return results

def process_dxl_files(folder_path):
    """
    Process all DXL files in the specified folder.
    
    Args:
        folder_path: Path to the folder containing DXL files
    
    Returns:
        Dictionary with file names as keys and extracted items as values
    """
    folder = Path(folder_path)
    
    # Check if folder exists
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Folder not found: {folder_path}")
    
    all_results = {}
    
    # Find all .dxl files in the folder
    dxl_files = list(folder.glob('**/*.dxl'))
    
    if not dxl_files:
        print(f"No .dxl files found in {folder_path}")
        return all_results
    
    # Process each file
    for file_path in dxl_files:
        try:
            results = extract_field_tx_6_items(file_path)
            if results:
                all_results[file_path.name] = results
            print(f"Processed {file_path.name} - Found {len(results)} Field_Tx_6 items")
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
    
    return all_results

def save_results_to_file(results, output_file="field_tx_6_results.txt"):
    """
    Save the extracted results to a text file.
    
    Args:
        results: Dictionary with file names and extracted items
        output_file: Path to the output file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_name, items in results.items():
            f.write(f"File: {file_name}\n")
            f.write("-" * 50 + "\n")
            
            for item_name, text in items.items():
                f.write(f"{item_name}: {text}\n\n")
            
            f.write("\n\n")

def extract_unique_text_values(results):
    """
    Extract unique text values from all Field_Tx_6 items.
    
    Args:
        results: Dictionary with file names and extracted items
    
    Returns:
        Set of unique text values
    """
    unique_values = set()
    for items in results.values():
        for text in items.values():
            unique_values.add(text)
    return sorted(unique_values)

def save_unique_values_to_file(unique_values, output_file="unique_text_values.txt"):
    """
    Save unique text values to a file.
    
    Args:
        unique_values: Set of unique text values
        output_file: Path to the output file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for value in unique_values:
            f.write(f"{value}\n")

def extract_deterioration_tx_items(file_path):
    """
    Extract text from items with name 'Deterioration_Tx_{number}' in a DXL file.
    
    Args:
        file_path: Path to the DXL file
    
    Returns:
        Dictionary with item names as keys and their text content as values
    """
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Since DXL files might not be well-formed XML, use regex to extract items
    pattern = r'<item\s+name=[\'"]Deterioration_Tx_(\d+)[\'"]>\s*<text>(.*?)</text>\s*</item>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    results = {}
    for number, text in matches:
        item_name = f'Deterioration_Tx_{number}'
        # Clean up the text - replace <break/> with newlines and remove extra whitespace
        clean_text = re.sub(r'<break\s*/>', '\n', text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        results[item_name] = clean_text
    
    return results

def process_deterioration_files(folder_path):
    """
    Process all DXL files in the specified folder for Deterioration_Tx items.
    
    Args:
        folder_path: Path to the folder containing DXL files
    
    Returns:
        Dictionary with file names as keys and extracted items as values
    """
    folder = Path(folder_path)
    
    # Check if folder exists
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Folder not found: {folder_path}")
    
    all_results = {}
    
    # Find all .dxl files in the folder
    dxl_files = list(folder.glob('**/*.dxl'))
    
    if not dxl_files:
        print(f"No .dxl files found in {folder_path}")
        return all_results
    
    # Process each file
    for file_path in dxl_files:
        try:
            results = extract_deterioration_tx_items(file_path)
            if results:
                all_results[file_path.name] = results
            print(f"Processed {file_path.name} - Found {len(results)} Deterioration_Tx items")
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
    
    return all_results

def main():
    # Set the folder path containing DXL files
    folder_path = "RBI_sample"
    
    try:
        # Process the DXL files for Field_Tx_6 items
        field_results = process_dxl_files(folder_path)
        
        if field_results:
            # Print summary for Field_Tx_6
            total_field_items = sum(len(items) for items in field_results.values())
            print(f"\nFound {total_field_items} Field_Tx_6 items in {len(field_results)} files.")
            
            # Save detailed results to file
            field_output_file = "field_tx_6_results.txt"
            save_results_to_file(field_results, field_output_file)
            print(f"Detailed Field_Tx_6 results saved to {field_output_file}")
            
            # Extract and save unique values for Field_Tx_6
            field_unique_values = extract_unique_text_values(field_results)
            field_unique_output_file = "unique_field_tx_6_values.txt"
            save_unique_values_to_file(field_unique_values, field_unique_output_file)
            print(f"Found {len(field_unique_values)} unique Field_Tx_6 text values")
            print(f"Unique Field_Tx_6 values saved to {field_unique_output_file}")
        
        # Process the DXL files for Deterioration_Tx items
        deterioration_results = process_deterioration_files(folder_path)
        
        if deterioration_results:
            # Print summary for Deterioration_Tx
            total_deterioration_items = sum(len(items) for items in deterioration_results.values())
            print(f"\nFound {total_deterioration_items} Deterioration_Tx items in {len(deterioration_results)} files.")
            
            # Save detailed results to file
            deterioration_output_file = "deterioration_tx_results.txt"
            save_results_to_file(deterioration_results, deterioration_output_file)
            print(f"Detailed Deterioration_Tx results saved to {deterioration_output_file}")
            
            # Extract and save unique values for Deterioration_Tx
            deterioration_unique_values = extract_unique_text_values(deterioration_results)
            deterioration_unique_output_file = "unique_deterioration_tx_values.txt"
            save_unique_values_to_file(deterioration_unique_values, deterioration_unique_output_file)
            print(f"Found {len(deterioration_unique_values)} unique Deterioration_Tx text values")
            print(f"Unique Deterioration_Tx values saved to {deterioration_unique_output_file}")
        
        if not field_results and not deterioration_results:
            print("No items found in any files.")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()