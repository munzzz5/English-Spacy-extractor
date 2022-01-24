import pandas as pd
import spacy


nlp = spacy.load("en_core_web_md")


def getWordData(doc, inword):

    dictWord = [{'word': word.text, 'POS': word.pos_, 'DEP': word.dep_, 'left': [tok.text if tok else 0 for tok in word.lefts], 'right': [
        tok.text if tok else 0 for tok in word.rights], 'lemma': word.lemma_} for word in doc if word.text == inword]
    return dictWord[0]


def getExcel(fileName):
    df = pd.read_excel(fileName)
    return df


def saveAndExit(outDf):
    print(len(outDf['Task']), len(outDf['word']), len(outDf['POS']), len(
        outDf['DEP']), len(outDf['lemma']), len(outDf['left']), len(outDf['right']))
    print('saving and exiting\n')
    pd.DataFrame(outDf).to_excel(
        input('Enter file to save')+".xlsx")
    exit()


def getColumnAndExtract():
    tasks = df[input('Enter the column name: ')]

    outDf = {'Task': [], 'word': [], 'POS': [],
             'DEP': [], 'lemma': [], 'left': [], 'right': []}
    for task in tasks:
        print(task)
        doc = nlp(task)
        # print(doc['check'].lemma_)

        wordList = [token.text for token in doc]
        # 1. ask user for important words
        # 2. if word in doc, get meaning, add to list
        # 3. break with x
        # 4. return list
        firstWord = True
        while(True):
            inputWord = input(
                "Enter word: (Enter 1 for next task||Enter 2 to stop completely and save your work)")

            if inputWord == '1':  # break keyword
                print('next task\n')
                firstWord = False
                break
            elif inputWord == '2':  # exit keyword
                saveAndExit(outDf)
            if inputWord in wordList:

                dTemp = getWordData(doc, inputWord)
                if not firstWord:
                    outDf['Task'].append('')
                else:
                    outDf['Task'].append(task)
                    firstWord = False
                for key in dTemp:
                    outDf[key].append(dTemp[key])

            else:
                print("Word isnt there! Try again\n\n")
                continue
    saveAndExit(outDf)


if __name__ == "__main__":
    df = getExcel(input("Enter the file name: "))
    getColumnAndExtract()
