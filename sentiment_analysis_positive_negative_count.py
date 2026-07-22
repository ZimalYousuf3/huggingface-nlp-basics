!pip install transformers -q             # setting up transformers library from huggingface
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

reviews = [ 'I love this course. ',
           'I hate coding. ',
           'This class is too boring. ',
           'I hate being a CS student. '
           ]

results = classifier(reviews)
positive = 0
negative = 0

for review, result in zip(reviews, results):
  print(f'{result["label"]} ({result["score"]:.2f}) -> {review} \n')

  if result["label"] == "POSITIVE":
    positive +=1
  else:
    negative +=1

print(f'Positive: {positive}')
print(f'Negative: {negative}')
