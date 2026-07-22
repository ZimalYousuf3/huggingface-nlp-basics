from huggingface_hub import InferenceClient # importing InferenceClient Library from huggingface_hub without downloading

client = InferenceClient( token = " YOUR_HF_TOKEN" )

result = client.text_classification('I love python', model = 'distilbert-base-uncased-finetuned-sst-2-english')

print(result)
