import openai
import whisper
import os
import PyPDF2
import textract
from pydub import AudioSegment

# TODO: url so that sites can be read, fix pptx and xlsx files

openai.api_key = os.getenv("OPENAI_API_KEY")
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

def read_text(file_path):
    lines = ""
    if file_path.endswith(".pdf"):
        file = open(file_path, 'rb')
        PDFreader = PyPDF2.PdfReader(file)
        for pageObj in PDFreader.pages:
            lines += pageObj.extract_text()

    elif file_path.endswith(".docx"):
        lines = textract.process(file_path).decode('utf-8')  

    elif file_path.endswith(".mp3"):
        file = open(file_path, 'rb')
        if os.path.getsize(file_path) /1024**2 > 25: # if file is bigger than 25 MB
            directory, file = os.path.split(path)
            os.chdir(directory)
            audio_file = AudioSegment.from_mp3(file)
            min_15 = 15*60*1000
            audio_min_15 = [audio_file[i:i+min_15] for i in range(0, len(audio_file), min_15)]
            num = 0

            for audio_part in audio_min_15:
                num += 1 
                audio_part.export(f"Audiofile{num}.mp3", format="mp3")
                audio_part_mp3 = open(f"Audiofile{num}.mp3", 'rb')
                lines += openai.Audio.transcribe("whisper-1", audio_part_mp3)['text']
                audio_part_mp3.close()
                os.remove(f"Audiofile{num}.mp3")

        else:
            lines = openai.Audio.transcribe("whisper-1", file)["text"]
        
        file.close()
    
    else:
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                lines += line
    
    return lines

print("Commands: To quit: exit/.q, read the text in the file: 'path' + .r  ")

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
        message = message + '\n' + read_text(path)
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
    print()
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
     