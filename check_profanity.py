import urllib.request

def read_text():
    quotes=open (r"C:\Users\NAVNEET\Downloads\movie_quotes.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(word_to_check):
    connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+word_to_check)
    output=connectio.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!!")
    elif "false" in output:
        print("document has no curse words!!")
    else:
        print("Couldn't scan the document")


read_text()
