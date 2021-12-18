from gtts import gTTS
import os
text1 ="Hello hiow are you"
lan ='en'
myobj =gTTS(text=text1,lang=lan,slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")