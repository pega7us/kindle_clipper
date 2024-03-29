from collections import namedtuple
import re

CLIPPING_END_INDICATOR = '==========\n'
with open('My Clippings.txt', 'r', encoding='utf-8-sig') as user_clippings:
    #READ user's clippings file and SPLIT individual clippings
    clippings = user_clippings.read().split(CLIPPING_END_INDICATOR)
    clippings.pop()

#SPLIT UP each individual clipping into a namedtuple (Title, Highlight) stored in a list
TITLE_AND_HIGHLIGHT = namedtuple('TITLE_AND_HIGHLIGHT', ['title', 'highlight'])
split_clippings = []

TITLE_INDEX = 0
HIGHLIGHT_INDEX = 3
BYTE_ORDER_MARK = '\ufeff'
LINE_BREAK = '\n'
for clipping in clippings:
    temporary_list = clipping.replace(BYTE_ORDER_MARK, '').split(LINE_BREAK)
    split_clippings.append(TITLE_AND_HIGHLIGHT(temporary_list[TITLE_INDEX], temporary_list[HIGHLIGHT_INDEX]))

sorted_clippings = {}
PUNCTUATION = ' ,.”'
SPACE = '\s'
#SORT clipping highlights into WORDS and PARAGRAPHS and add them to according TITLE
for clipping in split_clippings:
    
    if clipping.title not in sorted_clippings.keys():
        sorted_clippings[clipping.title] = {'words':[], 
                                            'paragraphs':[]}
        
    if len(re.findall(SPACE,clipping.highlight)) < 3:
        sorted_clippings[clipping.title]['words'].append(clipping.highlight.lower().strip(PUNCTUATION))
    else:
        sorted_clippings[clipping.title]['paragraphs'].append(clipping.highlight)

#WRITE sorted clippings to a new file
with open('clippings.txt', 'w') as output:
    
    #Write TITLEs
    for title in sorted_clippings:
        breaker = '-' * len(title)
        output.write('\n' + title + '\n' + breaker + '\n')
        
        #Write all WORDS in the TITLE
        for word in sorted_clippings[title]['words']:
            output.write(word + '\n')
            
        #Write all PARAGRAPHS in the TITLE
        for paragraph in sorted_clippings[title]['paragraphs']:
            output.write('\n' + '"' + paragraph + '"' + '\n')
