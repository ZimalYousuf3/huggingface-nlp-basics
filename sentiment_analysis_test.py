!pip install transformers -q             # setting up transformers library from huggingface
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

result_1 = classifier('I absolutely loved this course.') # Tokenization
print(result_1)

print()

result_2 = classifier('I absolutely hate this course.')
print(result_2)
