import pandas as pd
import spacy



nlp=spacy.load("en_core_web_md")

def getWordData(doc,inword):
    
    dictWord=[{'word':word.text,'POS':word.pos_,'DEP':word.dep_,'lemma':word.lemma_} for word in doc if word.text==inword]
    return dictWord[0]  

if __name__ == "__main__":
    df=pd.read_excel(input("Enter the file name with extension: "))
    tasks=df[input('Enter the column name: ')]

    outDf={'Task':[],'word':[],'POS':[],'DEP':[],'lemma':[]}
    for task in tasks:
        print(task)
        doc=nlp(task)
        # print(doc['check'].lemma_)
        outDf['Task'].append(task)
        wordList=[token.text for token in doc]
        # 1. ask user for important words
        # 2. if word in doc, get meaning, add to list
        # 3. break with x
        # 4. return list
        firstWord=True
        while(True):
            inputWord=input("Enter word: (Enter 1 for next task||Enter 2 to stop completely and save your work)")
            
            if inputWord=='1': #break keyword
                print('next task\n')
                firstWord=False
                break
            elif inputWord=='2':
                print(outDf)
                print('saving and exiting\n')
                pd.DataFrame(outDf).to_excel(input('Enter file to save')+".xlsx")
                exit()
            if inputWord in wordList:
                dTemp=getWordData(doc,inputWord)
                if not firstWord:
                    outDf['Task'].append('')
                else:
                    firstWord=False
                for key in dTemp:
                    outDf[key].append(dTemp[key])
                
            else:
                print("Word isnt there! Try again\n\n")
                continue
            
    
          
