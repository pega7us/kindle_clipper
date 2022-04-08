from collections import namedtuple
import re

with open('My Clippings.txt', 'r', encoding='utf-8-sig') as user_clippings:
    #READ user's clippings file and SPLIT individual clippings
    clippings = user_clippings.read().split('==========\n')
    clippings.pop()

#SPLIT UP each individual clipping into a namedtuple (Title, Highlight) stored in a list
TITLE_AND_HIGHLIGHT = namedtuple('TITLE_AND_HIGHLIGHT', ['title', 'highlight'])
split_clippings = []

for clipping in clippings:
    temporary_list = clipping.replace('\ufeff', '').split('\n')
    split_clippings.append(TITLE_AND_HIGHLIGHT(temporary_list[0], temporary_list[3]))

sorted_clippings = {}
#SORT clipping highlights into WORDS and PARAGRAPHS and add them to according TITLE
for clipping in split_clippings:
    
    if clipping.title not in sorted_clippings.keys():
        sorted_clippings[clipping.title] = {'words':[], 
                                            'paragraphs':[]}
        
    if len(re.findall('\s',clipping.highlight)) < 3:
        sorted_clippings[clipping.title]['words'].append(clipping.highlight.lower().strip(' ,.”'))
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
