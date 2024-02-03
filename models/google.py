from googletrans import Translator


def googletrans_translator(user_input):
    translator = Translator()
    response_str = (translator.translate(user_input, src="pl", dest="en")).text
    return response_str
