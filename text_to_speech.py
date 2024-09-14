from gtts import gTTS
import os
text="hi hru , my name is asma "
language='en'
obj=gTTS(text= text,lang=language,slow=False)

obj.save("sample.mp3")

