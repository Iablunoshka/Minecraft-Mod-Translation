Minecraft Mods Russian Translator
This script automatically translates the English language files (en_us.json) found within Minecraft mods to Russian (ru_ru.json).

Description
The script works by iterating through the provided directory, searching for en_us.json files within .jar mod files. When found, it reads the English text from the JSON, translates it to Russian using the deep_translator package, and then writes the translated text back to a new ru_ru.json file in the .jar mod file.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python installed on your machine.
deep_translator Python package installed. Install it via pip:
bash
Copy code
pip install deep_translator
Usage
To run the script:

Navigate to the directory containing the script.
Run the script using:
bash
Copy code
python script_name.py -i /path/to/your/mods/directory
Replace script_name.py with the name of your Python script and /path/to/your/mods/directory with the path to the directory containing your Minecraft mod .jar files.

Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

License
This project is open-source. Feel free to use, modify, and distribute the code as you see fit.

You can copy and paste the above content into your README.md file when you create your GitHub repository. Make sure to adjust any details if necessary.
