# Source - https://stackoverflow.com/a/49285139
# Posted by titipata
# Retrieved 2026-05-05, License - CC BY-SA 3.0
import spacy
# Importing a python library to find Verbs and nouns
nlp = spacy.load("en_core_web_sm")
# importing a pretrained "English teacher"
text = input("Input the original text for your mad lib here")
# Getting orginal text to create mad lib from user
# Source - https://stackoverflow.com/a/49285139
# Posted by titipata
# Retrieved 2026-05-05, License - CC BY-SA 3.0




doc = nlp(text)

output_tokens = []

for token in doc:
    # Check if the token is a noun
    if token.pos_ == "NOUN":
        # Get replacement from player input
        replacement = input(f"Replace noun '{token.text}' with: ")
        output_tokens.append(replacement)
    else:
        output_tokens.append(token.text)
    
    # Preserve original whitespace
    output_tokens.append(token.whitespace_)

# Join tokens back into a final string
final_text = "".join(output_tokens)
for token in doc:
    # Check if the token is a noun
    if token.pos_ == "VERB":
        # Get replacement from player input
        replacement = input(f"Replace noun '{token.text}' with: ")
        output_tokens.append(replacement)
    else:
        output_tokens.append(token.text)
    
    # Preserve original whitespace
    output_tokens.append(token.whitespace_)

# Join tokens back into a final string
final_text = "".join(output_tokens)
print(final_text)


