from transformers import MBart50TokenizerFast, MBartForConditionalGeneration


def mbart_translator(user_input):
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer.src_lang = "pl_PL"

    encoded_pl = tokenizer(user_input, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_pl,
        forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
    )
    simulated_response1 = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    response_str = ' '.join(simulated_response1)
    return response_str
