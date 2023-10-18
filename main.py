import zipfile
import json
import os
from deep_translator import GoogleTranslator
import argparse

# Create a parser
parser = argparse.ArgumentParser(description="Translate Minecraft mods to Russian")

# Add arguments
parser.add_argument('-i', '--input', help='Path to the directory with mods', required=True)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your script
mods_directory = args.input

# Function to translate text to Russian
def translate_to_russian(text):
    return GoogleTranslator(source='auto', target='ru').translate(text)

# List files in the mods directory
files = os.listdir(mods_directory)


# Iterate through the files in the mods directory
for file in files:
    jar_file_path = os.path.join(mods_directory, file)

    try:
        # Open the JAR file and look for 'en_us.json' in the archive
        with zipfile.ZipFile(jar_file_path, 'a') as jar:
            en_us_json_paths = [name for name in jar.namelist() if name.endswith('/en_us.json')]

            if en_us_json_paths:
                # For each 'en_us.json' in the mod, create a corresponding path for 'ru_ru.json'
                for en_us_json_path in en_us_json_paths:
                    ru_ru_json_path = en_us_json_path.replace('/en_us.json', '/ru_ru.json')

                    # Check for the existence of 'ru_ru.json' before starting the loop
                    if not ru_ru_json_path in jar.namelist():
                        # Read the content of the JSON file as bytes
                        with jar.open(en_us_json_path) as json_file:
                            json_data = json_file.read()

                        # Decode the bytes of the JSON file into a dictionary
                        json_text = json_data.decode('utf-8')
                        json_dict = json.loads(json_text)

                        # Translate values to Russian and add them to the dictionary
                        translations = {}
                        for key, value in json_dict.items():
                            translated_text = translate_to_russian(value)
                            translations[key] = translated_text

                        # Create a new 'ru_ru.json' file in the archive
                        with jar.open(ru_ru_json_path, 'w') as ru_ru_file:
                            ru_ru_json = json.dumps(translations, ensure_ascii=False, indent=4)
                            ru_ru_bytes = ru_ru_json.encode("utf-8")
                            ru_ru_file.write(ru_ru_bytes)

                        # Print a message when the translation is completed
                        print(f"'ru_ru.json' files added to {jar_file_path}")
                    else:
                        # Print a message that 'ru_ru.json' already exists
                        print(f"'ru_ru.json' already exists in {jar_file_path}. No translation needed.")
                        
    except Exception as e:
        # Print a message for skipping the mod in case of an error or missing 'en_us.json'
        print(f"Mod '{jar_file_path}' skipped: {str(e)}")
        continue
