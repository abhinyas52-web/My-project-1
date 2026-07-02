from transformers import pipeline 
classifier = pipeline("image-classification")
result = classifier(#path of your image)
print(result)
