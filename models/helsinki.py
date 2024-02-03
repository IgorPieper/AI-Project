from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def helsinki_translator(user_input):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pl-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-pl-en")

    encoded_pl = tokenizer(user_input, return_tensors="pt")
    output = model.generate(**encoded_pl)
    response_str = tokenizer.decode(output[0], skip_special_tokens=True)
    return response_str
