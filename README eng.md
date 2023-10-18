# Automatic Translation of Minecraft Mods to Russian

The script operates by scanning the provided directory for en_us.json files within .jar mod files. When found, it reads the English text from the JSON, translates it into Russian using the deep_translator package, and then writes the translated text back into a new ru_ru.json file within the .jar mod file.

## Usage

To use the script, follow these steps:

1. Ensure you have Python 3 installed.
2. Install the required dependencies.
3. Run the script with the path to the directory containing the mods you want to translate:

   ```bash
   python main.py -i PATH_TO_MODS_DIRECTORY
   ```

4. The script will automatically translate the text in the mods and create files in Russian.

## Features

- The script works for most versions of Minecraft.
- It autonomously detects if a mod has Russian localization; if it does, it skips it.
- If a mod lacks en_us.json, it won't be translated and will be skipped.

## Dependencies

To run the script, you'll need the following libraries:

- `deep_translator`
- `argparse`
- `zipfile`
- `json`

## Important

- This script utilizes Google Translator, which may have limitations or rate limits. Be mindful of these restrictions when translating a large number of mods.

- Some mods may not have "en_us.json" files, or the translation may be imperfect due to automatic translation.

- Before running this script, ensure you have backups of your mods, as it alters mods by adding translated files.

## License

This project is distributed under the MIT license. Details can be found in the [LICENSE](LICENSE) file.

## Author

Author: @Iablunoshka

## Contact

If you have questions or suggestions, feel free to reach out to me on Discord: 6masia9
