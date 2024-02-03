from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def nllb_translator(user_input):
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
    tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    tokenizer.src_lang = "pl_PL"

    encoded_pl = tokenizer(user_input, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_pl,
        forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"]
    )
    simulated_response1 = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    response_str = ' '.join(simulated_response1)
    return response_str
