import nltk
from nltk.corpus import wordnet 
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import re
sp = spacy.load('en_core_web_sm')

def removing_shortcuts(text):
    full_words = []
    shortcuts = {'u': 'you', 'y': 'why', 'r': 'are', 'doin': 'doing', 'hw': 'how', 'k': 'okay', 'm': 'am',
                 'b4': 'before',
                 'idc': "i do not care", 'ty': 'thank you', 'wlcm': 'welcome', 'bc': 'because', '<3': 'love',
                 'xoxo': 'love',
                 'ttyl': 'talk to you later', 'gr8': 'great', 'bday': 'birthday', 'awsm': 'awesome', 'gud': 'good',
                 'h8': 'hate',
                 'lv': 'love', 'dm': 'direct message', 'rt': 'retweet', 'wtf': 'hate', 'idgaf': 'hate',
                 'irl': 'in real life', 'yolo': 'you only live once', "don't": "do not", 
                 "won't": "will not", 'tbh': 'to be honest', 'caj': 'casual', 'Ikr': 'I know, right?',
                 'omw': 'on my way',
                 'ofc': 'of course', 'Idc': "I don't care", 'Irl': 'In real life', 'tbf': 'To be fair',
                 'obvs': 'obviously', 'v': 'very', 'atm': 'at the moment',
                 'col': 'crying out loud', 'gbu': 'god bless you', 'gby': 'god bless you', 'gotcha': 'I got you',
                 'hehe': 'laughing', 'haha': 'laughing', 'hf': 'have fun',
                 'hry': 'hurry', 'hw': 'hardwork', 'idc': 'i don’t care', 'ikr': 'i know right', 'k': 'ok',
                 'lmao': 'laughing my ass off', 'lol': 'laughing out loud',
                 'n1': 'nice one', 'na': 'not available', 'qt': 'cutie', 'qtpi': 'cutie pie', 'rip': 'rest in peace',
                 'sry': 'sorry', 'tc': 'take care',
                 'thnks': 'thanks', 'thx': 'thanks', 'thnk': 'thanks', 'txt': 'text',
                 'ugh': 'disgusted', 'w8': 'wait', "not sad": "happy","didn't":"did not","couldn't":"could not",
                 "wouldn't":"would not","shouldn't":"should not","doesn't":"does not"}

    for token in text:
        if token in shortcuts.keys():
            token = shortcuts[token]
        full_words.append(token)
    text = " ".join(full_words)
    return text

def checksimilarity(word,list1):
    try:
        word=wordnet.synsets(word)
        name=wordnet.synset(word[0].name())
        for i in range(len(list1)):
            w1=wordnet.synsets(list1[i])
            name=wordnet.synset(w1[0].name())
            name2=w1[0].name()
            if((name.wup_similarity(name2))>=0.5):
                return True
            else:
                return False
    except Exception as e:
        return False

def removing_not(text):
    d = {'not sad': 'Happy', 'not bad': 'Happy', 'not boring': 'Happy', 'not wrong': 'Happy', 'not bored': 'Happy',
         'not jealous': 'Happy', 'not happy': 'Sad', 'not well': 'Sad', 'not suitable': 'Angry', 'not right': 'Angry',
         'not good': 'Sad', 'not excited': 'Angry', 'not funny ': 'Sad', 'not  kind': 'Sad', 'not proud': 'Angry',
         'not cool': 'Angry', 'not funny': 'Angry', 'not kind': 'Angry', 'not open': 'Angry', 'not safe': 'Fear',
         'not enough': 'Empty', 'not know': 'Sad', 'not knowing': 'Sad', 'not believe': 'Angry',
         'not believing': 'Angry',
         'not understand': 'Sad', 'not understanding': 'Sad', 'no doubt': 'Happy', 'not think': 'Sad',
         'not thinking': 'Sad',
         'not recognise': 'Sad', 'not recognising': 'Sad', 'not forget': 'Angry', 'not forgetting': 'Angry',
         'not remember': 'Sad',
         'not remembering': 'Sad', 'not imagine': 'Sad', 'not imagining': 'Sad', 'not mean': 'Sad',
         'not meaning': 'Sad',
         'not agree': 'Angry', 'not agreeing': 'Sad', 'not disagree': 'Happy', 'not disagreeing': 'Happy',
         'not deny': 'Sad',
         'not denying': 'Sad', 'not promise': 'Angry', 'not promising': 'Angry', 'not satisfy': 'Sad',
         'not satisfying': 'Sad',
         'not realise': 'Sad', 'not realising': 'Sad', 'not appear': 'Angry', 'not appearing': 'Angry',
         'not please': 'Sad', 'not pleasing': 'Sad', 'not impress': 'Sad', 'not impressing': 'Sad',
         'not surprise': 'Sad', 'not surprising': 'Sad', 'not concern': 'Sad', 'not concerning': 'Sad',
         'not have': 'Sad', 'not having': 'Sad',
         'not own': 'Sad', 'not owning': 'Sad', 'not possess': 'Sad', 'not possessing': 'Sad', 'not lack': 'Sad',
         'not lacking': 'Sad',
         'not consist': 'Sad', 'not consisting': 'Sad', 'not involve': 'Sad', 'not involving': 'Sad',
         'not include': 'Sad', 'not including': 'Sad', 'not contain': 'Sad',
         'not containing': 'Sad', 'not love': 'Sad', 'not like': 'Angry',
         'not hate': 'Happy', 'not hating': 'Happy', 'not adore': 'Sad', 'not adoring': 'Sad', 'not prefer': 'Sad',
         'not preferring': 'Sad', 'not care': 'Angry', 'not mind': 'Angry', 'not minding': 'Sad',
         'not want': 'Angry', 'not wanting': 'Sad',
         'not need': 'Angry', 'not needing': 'Angry', 'not desire': 'Sad', 'not desiring': 'Sad', 'not wish': 'Sad',
         'not wishing': 'Sad', 'not hope': 'Sad', 'not hoping': 'Sad', 'not appreciate': 'Sad',
         'not appreciating': 'Sad',
         'not value': 'Sad', 'not valuing': 'Sad', 'not owe': 'Sad', 'not owing': 'Sad', 'not seem': 'Sad',
         'not seeming': 'Sad', 'not fit': 'Sad', 'not fitting': 'Sad', 'not depend': 'Sad',
         'not depending': 'Sad', 'not matter': 'Sad', 'not afford': 'Sad', 'not affording': 'Sad', 'not aim': 'Sad',
         'not aiming': 'Sad', 'not attempt': 'Angry', 'not attempting': 'Angry', 'not ask': 'Angry',
         'not asking': 'Angry', 'not arrange': 'Angry', 'not arranging': 'Angry', 'not beg': 'Angry',
         'not begging': 'Angry', 'not begin': 'Angry', 'not beginning': 'Angry', 'not caring': 'Angry',
         'not choose': 'Angry', 'not choosing': 'Angry', 'not claim': 'Angry', 'not claiming': 'Angry',
         'not consent': 'Angry', 'not consenting': 'Angry', 'not continue': 'Angry', 'not continuing': 'Angry',
         'not dare': 'Angry', 'not daring': 'Angry', 'not decide': 'Sad',
         'not deciding': 'Sad', 'not demand': 'Angry', 'not demanding': 'Angry', 'not deserve': 'Angry',
         'not deserving': 'Angry', 'not expect': 'Angry',
         'not expecting': 'Angry', 'not fail': 'Happy', 'not failing': 'Happy', 'not get': 'Sad', 'not getting': 'Sad',
         'not hesitate': 'Sad', 'not hesitating': 'Sad', 'not hurry': 'Happy', 'not hurrying': 'Happy',
         'not intend': 'Sad', 'not intending': 'Sad', 'not learn': 'Angry', 'not learning': 'Angry',
         'not liking': 'Angry', 'not loving': 'Sad', 'not manage': 'Angry',
         'not managing': 'Angry', 'not neglect': 'Sad', 'not neglecting': 'Sad', 'not offer': 'Angry',
         'not offering': 'Angry',
         'not plan': 'Angry', 'not planing': 'Angry', 'not prepare': 'Angry',
         'not preparing': 'Angry', 'not pretend': 'Angry', 'not pretending': 'Angry', 'not proceed': 'Angry',
         'not proceeding': 'Angry',
         'not propose': 'Angry', 'not proposing': 'Sad', 'not refuse': 'Sad', 'not refusing': 'Sad',
         'not start': 'Sad',
         'not starting': 'Sad', 'not stop': 'Happy', 'not stopping': 'Happy', 'not struggle': 'Angry',
         'not struggling': 'Angry',
         'not swear': 'Angry', 'not swearing': 'Angry', 'not threaten': 'Happy', 'not threatening': 'Happy',
         'not try': 'Angry', 'not trying': 'Angry', 'not volunteer': 'Angry',
         'not volunteering': 'Angry', 'not wait': 'Angry', 'not waiting': 'Angry', 'not feel': 'Sad',
         'not feeling': 'Sad', "not able": "Sad", "not do": "Sad","not want":"Sad","not go":"fear" }

    f = re.findall("not\s\w+", text)
    for i in f:
        try:
            text = text.replace(i, d[i])
        except:
            pass
    text = text.lower()
    return text
    
sen=input("Enter the sentence: ").lower()
sen=sen.split(" ")

sen=removing_shortcuts(sen)#removing shortcuts

sen=removing_not(sen)#removing not words and replacing it with emotions

swords=set(stopwords.words("english"))#removing unwanted words from sentence
sen1=[]
sen=word_tokenize(sen)#tokenizing in words
for word in sen:
    if word.lower() not in swords:
        sen1.append(word)
        

sentence=sp(str(sen1))
happy_val=0
sad_val=0
fear_val=0
disgust_val=0
anger_val=0
suprise_val=0
embarrassment_val=0
reactive_val=0
file2=open("happy.txt","r")
output=file2.read()
happy=output.split(',')
file2.close()
#print(happy)
file2=open("sad.txt","r")
output=file2.read()
sad=output.split(',')
file2.close()
#print(sad)
file2=open("fear.txt","r")
output=file2.read()
fear=output.split(',')
file2.close()
#print(fear)
file2=open("disgust.txt","r")
output=file2.read()
disgust=output.split(',')
file2.close()
#print(disgust)
file2=open("anger.txt","r")
output=file2.read()
angry=output.split(',')
file2.close()
#print(angry)
file2=open("suprise.txt","r")
output=file2.read()
suprise=output.split(',')
file2.close()
#print(suprise)
file2=open("embarrassment.txt","r")
output=file2.read()
embarrassment=output.split(',')
file2.close()
#print(embarrassment)
file2=open("reactive.txt","r")
output=file2.read()
reactive=output.split(',')
file2.close()
#print(reactive)

for word in sentence:
    syn=[]
    if(word.pos_!="PRON" and word.pos_!="DET"):
        for synset in wordnet.synsets(str(word)):
            for lemma in synset.lemmas():
                if lemma.name() not in syn:
                    if lemma.name() in happy or checksimilarity(lemma.name(),happy):
                        happy_val=happy_val+1
                    if lemma.name() in sad or checksimilarity(lemma.name(),sad):
                        sad_val=sad_val+1
                    if lemma.name() in angry or checksimilarity(lemma.name(),angry):
                        anger_val=anger_val+1
                    if lemma.name() in fear or checksimilarity(lemma.name(),fear):
                        fear_val=fear_val+1
                    if lemma.name() in disgust or checksimilarity(lemma.name(),disgust):
                        disgust_val=disgust_val+1
                    if lemma.name() in suprise or checksimilarity(lemma.name(),suprise):
                        suprise_val=suprise_val+1
                    if lemma.name() in embarrassment or checksimilarity(lemma.name(),embarrassment):
                        embarrassment_val=embarrassment_val+1
                    if lemma.name() in reactive or checksimilarity(lemma.name(),reactive):
                        reactive_val=reactive_val+1
                    syn.append(lemma.name())

maximum=max(happy_val,sad_val,anger_val,disgust_val,suprise_val,fear_val,embarrassment_val,reactive_val)  
if(maximum==happy_val==sad_val==anger_val==disgust_val==suprise_val==fear_val==embarrassment_val==reactive_val):
    print("The given sentence is neutral")
else:
    if(maximum==happy_val):
        print("\nThe given sentence belongs to happy")
    if(maximum==sad_val):
        print("\nThe given sentence belongs to sad")
    if(maximum==anger_val):
        print("\nThe given sentence belongs to angry")
    if(maximum==disgust_val):
        print("\nThe given sentence belongs to disgust")
    if(maximum==suprise_val):
        print("\nThe given sentence belongs to suprise")
    if(maximum==fear_val):
        print("\nThe given sentence belongs to fear")
    if(maximum==embarrassment_val):
        print("\nThe given sentence belongs to embarrassment")
    if(maximum==reactive_val):
        print("\nThe given sentence belongs to reactive")