from transformers import pipeline 
classifier = pipeline("image-classification")
result = classifier("/cat.jpg")
print(result)
