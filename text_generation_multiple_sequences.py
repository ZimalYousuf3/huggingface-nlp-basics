!pip install transformers -q             # setting up transformers library from huggingface
from transformers import pipeline

generator = pipeline('text-generation', model = 'distilgpt2')

out = generator('Learning python is ', max_length = 20, num_return_sequences = 2)

print(out[0]['generated_text'])
print(out[1]['generated_text'])
