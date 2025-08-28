import json

def merge_dictionaries(vietnamese_data, english_data):
    # Create a dictionary for Vietnamese entries, keyed by kanji
    viet_dict = {entry[0]: entry for entry in vietnamese_data if entry}
    
    # Process English entries, adding Vietnamese data where applicable
    merged_entries = []
    for eng_entry in english_data:
        kanji = eng_entry[0]
        # Skip if kanji not in Vietnamese dictionary
        if kanji not in viet_dict:
            continue
            
        viet_entry = viet_dict[kanji]
        # Create a new entry copying the English entry
        new_entry = eng_entry.copy()
        # Add Vietnamese meanings (index 4) and Radical (from metadata at index 5)
        new_entry[5] = new_entry[5].copy()  # Copy metadata dict to avoid modifying original
        new_entry[5]["vietnamese"] = viet_entry[4]  # Add Vietnamese meanings
        new_entry[5]["Radical"] = viet_entry[5]["Radical"]  # Add Radical
        
        merged_entries.append(new_entry)
    
    return merged_entries

# Load input files
with open('vietnamese.json', 'r', encoding='utf-8') as f:
    vietnamese_data = json.load(f)
with open('english.json', 'r', encoding='utf-8') as f:
    english_data = json.load(f)

# Merge dictionaries
merged_data = merge_dictionaries(vietnamese_data, english_data)

# Save output
with open('merged_dictionary.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)

print("Merged dictionary saved as 'merged_dictionary.json'")