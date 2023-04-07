import VoiceRecognition as VR
import DrawShapes as DS
while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    elif(text == "done"):
        break
    elif(text == "round"):
        print("Here")
        DS.DrawCircle()
    elif(text == "circle"):
        DS.TangentCircle()
    elif(text == "clear"):
        DS.ClearDrawings()
    else:
        print("Hai")

