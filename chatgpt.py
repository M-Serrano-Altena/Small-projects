import openai
import os
import PyPDF2
import textract

openai.api_key = os.getenv("OPENAI_API_KEY")
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

def read_code(file_path):
    lines = ""
    if file_path.endswith(".pdf"):
        file = open(file_path, 'rb')
        PDFreader = PyPDF2.PdfReader(file)
        for pageObj in PDFreader.pages:
            lines += pageObj.extract_text()

    elif file_path.endswith(".docx"):
        lines = textract.process(file_path).decode('utf-8')       
    
    else:
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                lines += line
    return lines


while True:
    message = input("User : ")
    if message.casefold() == "exit" or message == ".q":
       break

    if ("C:" in message) and ("Users" in message):
        for word in message.split('"'):
            if ("C:" in word) and ("Users" in word):
                path = word
        path = path.replace('"', '')

    if (".r" in message.casefold()):
        message = message + '\n' + read_code(path)
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    elif message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
     