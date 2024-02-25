import gtts
import playsound
import os
print('Welcome to our speaking world')

text = input('Enter what you want me to speak: ')
sound = gtts.gTTS(text, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")
os.remove("welcome.mp3")