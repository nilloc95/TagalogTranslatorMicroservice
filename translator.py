import time
from translate import Translator

tagalog_code = 'tl'
english_code = 'en'

translator_to_tagalog = Translator(to_lang="tl")
translator_to_english = Translator(from_lang = 'tl', to_lang="en")

english_to_tagalog_file_in = "from_eng_to_tagalog_in.txt"
english_to_tagalog_file_out = "from_eng_to_tagalog_out.txt"

tagalog_to_english_file_in = "from_tagalog_to_eng_in.txt"
tagalog_to_english_file_out = "from_tagalog_to_eng_out.txt"

while True:
    flag = False
    translation_to_tagalog = ""
    translation_to_english = ""
    while flag == False:
        time.sleep(1)
        with open(english_to_tagalog_file_in, "r") as f:
            content = f.read()
            if content != "":
                try:
                    translation_to_tagalog = translator_to_tagalog.translate(content)
                    flag = True
                except:
                    continue
        with open(tagalog_to_english_file_in, "r") as f:
            content = f.read()
            if content != "":
                try:
                    translation_to_english = translator_to_english.translate(content)
                    flag = True
                except:
                    continue
        

    with open(english_to_tagalog_file_in, "w") as f:     
        f.write("")  
    with open(tagalog_to_english_file_in, "w") as f:     
        f.write("")  
    with open(english_to_tagalog_file_out, "w") as f:
        print(translation_to_tagalog)
        f.write(translation_to_tagalog)
    with open(tagalog_to_english_file_out, "w") as f:
        print(translation_to_english)
        f.write(translation_to_english)
