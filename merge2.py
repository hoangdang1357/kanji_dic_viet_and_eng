import json

def merge_bank_2(vietnamese_file, english_file, output_file):
    """Merge Vietnamese reading (index 1) and Radical into English kanji_bank_2.json."""
    # Load files
    try:
        with open(vietnamese_file, 'r', encoding='utf-8') as f:
            vietnamese_data = json.load(f)
        with open(english_file, 'r', encoding='utf-8') as f:
            english_data = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}. Skipping.")
        return

    # Create dictionary for Vietnamese entries, keyed by kanji
    viet_dict = {entry[0]: entry for entry in vietnamese_data if entry}

    # Merge entries
    merged_entries = []
    for eng_entry in english_data:
        kanji = eng_entry[0]
        if kanji not in viet_dict:
            continue  # Skip if kanji not in Vietnamese dictionary
        viet_entry = viet_dict[kanji]
        # Create a new entry copying the English entry
        new_entry = eng_entry.copy()
        new_entry[5] = new_entry[5].copy()  # Copy metadata dict
        new_entry[5]["vietnamese"] = viet_entry[1]  # Add Vietnamese reading from index 1
        new_entry[5]["Radical"] = viet_entry[5]["Radical"]  # Add Radical
        merged_entries.append(new_entry)

    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_entries, f, indent=4, ensure_ascii=False)
    print(f"Merged dictionary saved as '{output_file}'")

# Merge kanji_bank_2.json
merge_bank_2('kanji_bank_2_viet.json', 'kanji_bank_2_eng.json', 'merged_kanji_bank_2.json')