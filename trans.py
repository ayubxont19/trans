from googletrans import Translator

translator = Translator()

def trans_bot(text):
    try:
        result = translator.translate(text)
        return result.text
    except:
        return f"Kechirasiz ({text}) so'zini tarjima qila olmadim"