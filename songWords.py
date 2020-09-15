songs = ["dynamite.txt", "before-you-go.txt"]

#Characters to filter out: ' , ? ( ) -
for song in songs:
    songFile = open(song, "r")
    lengthtoFreq = {}
    for lines in songFile:
        for word in lines.split():
            special =0
            for char in word:
                if char=="'" or char=="," or char=="?" or char=="(" or char==")" or char=="-":
                        special +=1
            wordLength = len(word) - special 
            if wordLength in lengthtoFreq:
                lengthtoFreq[wordLength] += 1
            else:
                lengthtoFreq[wordLength] = 1
    print(song.upper())
    print(lengthtoFreq)




            


