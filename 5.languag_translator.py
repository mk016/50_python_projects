from googletrans import Translator, LANGUAGES

def translate_text(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

def print_supported_languages():
    print("Supported Languages:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")

text = input("Enter the text you want to translate: ")
print_supported_languages()
target_lang = input("Enter the code of the target language: ")

if target_lang in LANGUAGES:
    translated_text = translate_text(text, target_lang)
    print("Translated Text:", translated_text)
else:
    print("Invalid target language code.")
