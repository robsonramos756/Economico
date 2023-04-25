import unittest
import json
import speech_recognition as sr


class CommandRecognitionTest(unittest.TestCase):

    
    with open('Link.json', 'r', encoding='utf-8') as f:
        commands = json.load(f)

    def recognize_audio(self, audio_file):
      
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        return r.recognize_google(audio, language='pt-BR')

    def test_maior_economia(self):
        audio_file = 'Maior_economia.wav'
        expected_response = 'Estados Unidos'
        transcribed_text = self.recognize_audio(audio_file)
        response = self.find_command(transcribed_text)
        self.assertEqual(response, expected_response)

    def test_maior_bloco(self):
        audio_file = 'Maior_bloco.wav'
        expected_response = 'União Europeia'
        transcribed_text = self.recognize_audio(audio_file)
        response = self.find_command(transcribed_text)
        self.assertEqual(response, expected_response)

    def test_maior_queda(self):
        audio_file = 'Maior_queda.wav'
        expected_response = 'Venezuela'
        transcribed_text = self.recognize_audio(audio_file)
        response = self.find_command(transcribed_text)
        self.assertEqual(response, expected_response)

    def test_maior_alta(self):
        audio_file = 'Maior_alta.wav'
        expected_response = 'Níger'
        transcribed_text = self.recognize_audio(audio_file)
        response = self.find_command(transcribed_text)
        self.assertEqual(response, expected_response)

    def test_pib_global(self):
        audio_file = 'Pib_global_1.wav'
        expected_response = '87,65 trilhões USD (2019)'
        transcribed_text = self.recognize_audio(audio_file)
        response = self.find_command(transcribed_text)
        self.assertEqual(response, expected_response)

    @staticmethod
    def tokenize_question(question):
        
        #Tokeniza as perguntas 
        
        return question.lower().split()

    def find_command(self, question):
        
        #Encontra o comando 
    
        tokens = self.tokenize_question(question)
        for cmd, data in self.commands.items():
            cmd_tokens = self.tokenize_question(cmd)
            if set(cmd_tokens).issubset(set(tokens)):
                return data
        return "Comando não reconhecido!"


if __name__ == '__main__':
    unittest.main(exit=False)
