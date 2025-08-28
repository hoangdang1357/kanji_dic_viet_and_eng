import json

def convert_vietnamese_to_string(input_file, output_file):
    """Convert 'vietnamese' field from list to string in merged dictionary."""
    # Load merged file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}. Skipping.")
        return

    # Process entries
    converted_entries = []
    for entry in data:
        new_entry = entry.copy()
        new_entry[5] = new_entry[5].copy()  # Copy metadata dict
        vietnamese = new_entry[5].get("vietnamese")
        if isinstance(vietnamese, list):
            # Convert list to string, joining with ", "
            new_entry[5]["vietnamese"] = ", ".join(vietnamese) if vietnamese else ""
        # If already a string or not present, leave unchanged
        converted_entries.append(new_entry)

    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_entries, f, indent=4, ensure_ascii=False)
    print(f"Converted dictionary saved as '{output_file}'")

# Convert vietnamese field in merged_kanji_bank_2.json
convert_vietnamese_to_string('kanji_bank_1.json', 'converted_kanji_bank_1.json')
