## Import libraries
from docx import Document

## Open the document
document = Document("story.docx")

## For each paragraph in the document,
for parg in document.paragraphs:
    
    ## Replace text in paragraph
    parg.text = parg.text.replace("Little Red Riding Hood", "Lord Charls")
    parg.text = parg.text.replace("friendly ", "angry")

## Save the new document
document.save('story-silly.docx')