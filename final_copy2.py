
# coding: utf-8



import sys
import json
import random
from pprint import pprint



with open('messages_babs.json') as data_file:    
    data = json.load(data_file)

print("loading json data")

counter = 0 
content_Barbara = []

for x in range(1738):
    
    if 'Barbara Alencar' in data['messages'][x]['sender_name']:
        try:
            content_Barbara_single = data['messages'][x]['content']
            content_Barbara.append(content_Barbara_single)
            
            #print(data['messages'][x]['content'])
            
        except Exception as e:
            pass 
            #print(e)
        
    else:
        pass
        #print(data['messages'][x]['sender_name'])

print("content Barbara loaded")

content_Isa = []

for x in range(1738):
    
    if 'Isa Vento' in data['messages'][x]['sender_name']:
        try:
            content_Isa_single = data['messages'][x]['content']
            content_Isa.append(content_Isa_single)
            
        except Exception as e:
            pass
            #print(e)
        
    else:
        pass
        #xtra_data = data['messages'][x]['sender_name']


print("content Isa loaded")

messages_content = []
messages = data['messages']

for item in messages:
    if 'content' in item:
#         content = [item["content"] for item in messages]
        content = item["content"]
        #print(content)
        messages_content.append(content)
    else: 
        content = 'null'
        messages_content.append(content)



import re

ISA_CLEAN = [line.replace('\\n',' ').replace('\n\n',' ').replace('\n',' ') for line in content_Isa]
BABS_CLEAN = [line.replace('\\n',' ').replace('\n\n',' ') for line in content_Barbara]

Isa_clean_clean = [re.sub(r'http\S+', '', item) for item in ISA_CLEAN]
Babs_clean_clean = [re.sub(r'http\S+', '', item) for item in BABS_CLEAN]

all_lines_isa = ' '.join(Isa_clean_clean)
all_lines_babs = ' '.join(Babs_clean_clean)

jpeg_data = bytearray(open("landscape_2.jpg", "rb").read())
print(len(jpeg_data))

print("importing spacy and preparing noun chunks")

import spacy 
nlp = spacy.load('en_core_web_md')


doc_isa = nlp(all_lines_isa)
doc_babs = nlp(all_lines_babs)
isa_sentences_as_list = list(doc_isa.sents)
babs_sentences_as_list = list(doc_babs.sents)


noun_chunks_I = [item.text for item in doc_isa.noun_chunks]
noun_chunks_B = [item.text for item in doc_babs.noun_chunks]

noun_chunks_Isa = ", ".join(noun_chunks_I)
noun_chunks_Babs = ", ".join(noun_chunks_B)


set_noun_chunks_B = set(noun_chunks_B)
set_noun_chunks_I = set(noun_chunks_I)

noun_chunks_I_no_rep = list(set_noun_chunks_I )
noun_chunks_B_no_rep = list(set_noun_chunks_B )



# In[106]:
def get_input():
    inData = input('> ')
    if inData == 'x':
        sys.exit()
    else:
        num = int(inData)
        chunk_number(num)

##figure out how to clear da string!
def chunk_number(num):
    global counter
    

    B= []
    B.append(random.choice(noun_chunks_B_no_rep))
    for i in range(num):
        B.append(" and " + random.choice(noun_chunks_B_no_rep) +  "\n" )
        #print(' '.join(x))  
        FOUR_CHUNKS_B = list(' '.join(B)    )    


    # In[107]:


    #how to add an and to end of every random choice apart from the last 
    I= []
    I.append(random.choice(noun_chunks_I_no_rep))
    for i in range(num):
        I.append(" and " + random.choice(noun_chunks_I_no_rep) + "\n" )
        #print(' '.join(x))  
        FOUR_CHUNKS_I = list(' '.join(I))

    print((' '.join(B)) + "\n \n subtracted from \n \n \n" + (' '.join(I)))


    char_list_1 = [ord(ascii_char) for ascii_char in FOUR_CHUNKS_B]
    #print(char_list_1)

    char_list_2 = [ord(ascii_char) for ascii_char in FOUR_CHUNKS_I]
    #print(char_list_2)



    temporary_len = 0

    if (len(char_list_1) > len(char_list_2)):
          temporary_len = len(char_list_2)
    else:
        temporary_len = len(char_list_1)


  
    ascii_string_operations = []
    for i in range(temporary_len):   
    #for i in range(len(char_list_2)):
        ascii_string_operations.append((char_list_1[i] - char_list_2[i]))
        myList = [abs(x) for x in ascii_string_operations]
    #print(myList)



    

    ascii_results = [chr(i) for i in myList]
    result_as_string = "".join(ascii_results)
    
    if counter < 6:
        img_location_start = random.randint(200000, 2700000)
   
    else:
        print("..........IT's GONNA BREAK..........")
        img_location_start = random.randint(0, 20)

    
    img_location_stop = img_location_start + len(result_as_string)
    #print(result_as_string)

    my_str_as_bytes = str.encode(result_as_string)
    #jpeg_data = bytearray(open("goat.jpg", "rb").read())
    jpeg_data[img_location_start:img_location_stop] = my_str_as_bytes

    wait = input('glitch >')

    if wait == " " :
     open("landscape_2.jpg", "wb").write(jpeg_data)
    else:
        pass

    
    counter +=1
    print(counter)
    get_input()
    
    
get_input()