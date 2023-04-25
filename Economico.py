import speech_recognition as sr
import nltk
import json

with open('link.json', 'r', encoding='utf-8') as f:
    commands = json.load(f)

# Tokeniza as perguntas em palavras
def tokenize_question(question):
    return nltk.word_tokenize(question.lower())

# Encontra o comando correspondente à pergunta
def find_command(question, commands):
    tokens = tokenize_question(question)
    for cmd, data in commands.items():
        cmd_tokens = tokenize_question(cmd)
        if set(cmd_tokens).issubset(set(tokens)):
            return data
    return None


r = sr.Recognizer()


mic = sr.Microphone()

# Define a taxa de amostragem para o reconhecedor de fala
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)
with mic as source:
    r.adjust_for_ambient_noise(source)
    

while True:
   
    with mic as source:
        print("Faça uma pergunta para o econômico: ")
        audio = r.listen(source)

    try:
       
        question = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {question}")

        
        response = find_command(question, commands)
        if response:
            print(response)
        else:
            print("Comando não reconhecido!")

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError as e:
        print("Erro ao processar a fala; {0}".format(e))
