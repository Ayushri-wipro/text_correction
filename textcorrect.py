import re
import docx
from transformers import AutoTokenizer, T5ForConditionalGeneration


def normalize_text(filepath):
    doc = docx.Document(filepath)
    new_file_lines = []
    for i in doc.paragraphs:
       #print(i.text)
        string= i.text
        lower_string = string.lower()
        no_number_string = re.sub(r'\d+','',lower_string)
        no_punc_string = re.sub(r'[^\w\s]','', no_number_string) 
        no_wspace_string = no_punc_string.strip()
        new_file_lines.append(no_wspace_string)
        
    with open(filepath, 'w') as file1:
        file1.writelines(new_file_lines)

    
    correct_data(file1)

def correct_data(filepath):
    model_name = "flexudy/t5-base-multi-sentence-doctor" # you can specify the model size here
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    doc = docx.Document(filepath)
    new_file_lines = []
    for i in doc.paragraphs:
        #print(i.text)
        input_text = "repair_sentence:"+i.text+"context: {Azur is good platfo.}{Hari is planning to present a dashboard.} </s>"

        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        outputs = model.generate(input_ids, max_length=32, num_beams=1)

        sentence = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        new_file_lines.append(sentence)
        
    with open(filepath, 'w') as file1:
        file1.writelines(new_file_lines)
    
    
        #print(sentence)

normalize_text("/home/ayushri/Downloads/VirtualRoom1_2021-05-05.docx")
