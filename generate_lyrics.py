from transformers import pipeline

lyrics = pipeline('text-generation', model='thomasdehaene/gpt2-large-dutch-finetune-oscar-10m-3epoch',
                tokenizer='thomasdehaene/gpt2-large-dutch-finetune-oscar-10m-3epoch', config={'max_length': 800})

result = lyrics('Daar was hij dan.')[0]['generated_text']
print(result)