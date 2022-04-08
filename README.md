# Kindle Clipper
Overview
--------
Kindle e-book reader comes with a function that allows to highlight parts of text while reading. These highlights or clippings, as Kindle refers to them, are saved to 'My clippings.txt' located in Kindle/documents. Each clipping is stored in the order it is added in such format:
```
Tropic of Cancer (Miller, Henry)
- Your Highlight on page 1 | Location 398-399 | Added on Friday, January 28, 2022 3:53:48 PM

I am living at the Villa Borghese. There is not a crumb of dirt anywhere, nor a chair misplaced. We are all alone here and we are dead.
==========
```
Every clipping is added in this format, where Title is followed by Location | Time Stamp, an empty line, highlight, and breaker.

I wrote a script that takes 'My clippings.txt' and outputs a new text file with this format:
```
Title  
-----
words
paragraphs
  
Title  
-----
words
paragraphs
```
..and so on.

How it works
------------
#### Reading the file  
The script opens 'My clippings.txt' and splits individual clippings using the separator '==========\n', saving the resulting list of strings as *clippings*. Since the string we get from reading the original file ends with the character that we use to separate clippings, we end up with an empty string at the end of the list [..,  '']. Hence, that empty string is popped from the list on line 7.

#### Sorting clippings  
Then, a loop sorts through the list of strings where each string is an individual clipping, and splits each clipping into sub-parts. Only *title* and *highlight* are retained. They are saved as a pair inside a named tuple and appended to a new list called *split_clippings*. A temporary variable called *temporary_list* is used within the loop to transfer data.

#### Re-organizing 
A dictionary named *sorted_clippings* is created. The next loop sorts and adds *titles* and *highlights* to this dictionary. 
First, an if-statement determines whether a title already exists in the dictionary. If it does not, the script adds that title as a key in *sorted_clippings* and sets up another dictionary as its value, containing two empty lists: *words* and *paragraphs*, ready to be filled with highlights. The following if-statement determines whether each highlight is a word or a paragraph, adding them to appropriate lists in the dictionary's title.

#### Writing a new file
Once the clippings are sorted and organized in the dictionary, the script proceeds to write a new txt file called 'clippings.txt'. Yet another loop is used to write the file. It starts by writing the *title*, then all *words* under the title, and lastly all *paragraphs*, before proceeding to the next title until there are no more data to write. The result is a humanly formatted text file that is saved in the working directiry.









