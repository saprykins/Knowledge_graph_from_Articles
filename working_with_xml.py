# current version finds article's title, pdf link, all the authors from one record

import xml.etree.ElementTree as ET

tree = ET.parse(
    "./API_response_one_entry_only.xml"
)

root = tree.getroot()

"""
# provides some good results

# print("tag is", root.tag)  # returns "feed"
# print("text is", root.text)  # returns text is, didn't find in xml
# print("atr is", root.attribute)  # no attribute
for child in root:
    for grand_child in child:
        print(grand_child.tag) # some good results
        print(grand_child.text) # some good results
        print("----")
"""

for child in root:
    for grand_child in child:
        # title = grand_child.find('title')
        # print(title)
        # print(grand_child.tag)
        # print(grand_child.tag)

        # print(grand_child.text)
        # print(grand_child.tag)
        # print('--')

        # finds and updates article's link
        if grand_child.tag == '{http://www.w3.org/2005/Atom}id':
            article_link = grand_child.text
            pdf_link = article_link.replace(
                'http://arxiv.org/abs', 'http://arxiv.org/pdf')
            print(pdf_link)

        # prints title of article
        if grand_child.tag == '{http://www.w3.org/2005/Atom}title':
            print(grand_child.text)

        # printing authors
        # ::2 to avoid printing departments
        for grand_grand_child in grand_child[::2]:
            # acces to authors and their departments
            print(grand_grand_child.text)


"""
# short pause to find out how to print out only titles
for child in root:
    for grand_child in child:
        title = grand_child.find('title')
        
        # print(grand_child.tag) # some good results # need to go deeper to find link
        # print(grand_child.text) # contains title (3rd), but much more

        print(title)
        
        # print(grand_child.tag) # some good results # need to go deeper to find link
        # print(grand_child.text) # contains title (3rd)
        print('---')
        
        # printing authors
        # ::2 to avoid printing departments
        for grand_grand_child in grand_child[::2]:
            # acces to authors and their departments
            print(grand_grand_child.text) 
"""


"""
for entries in root.findall("entry/title"):
    value = entries.text
    print(value)
"""

"""
titles = tree.findall(".//title") # ничего не дает

for title in titles:
    print(type(title))
"""

"""
for child in root:  # level of articles
    for item in child:  # level of title, bad link and date
        # print(item.findall("./name"))

        # print(item.tag)
        
        '''
        # doesn't give authors
        for authors in item.findall("author"):
            author = authors.find("author").text
            print(author)
        '''
        # how to choose a tag=title (which gives the title of article)?
        # if item.tag == "title": # doesn't specify <title>
        # print(item.tag) # gives children
        # print(item.text) # gives title, bad links and much more
        # print(item.attribute) # gives {}
# print(root[0][0].text) # doesn't work because out of range
"""

'''
doesn't show anything
for article in root.findall("entry"):
    article_title = article.find("title").text
    article_bad_link = article.find("id").text
    print(article_title, article_bad_link)
'''
