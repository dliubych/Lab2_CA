__author__ = 'Maxim'


# Checks string for palindrome
def is_palindrome(string):
    for i in range(0, len(string) / 2 + len(string) % 2):
        if string[i] != string[len(string) - 1 - i] or string[i] == ' ':
            return False
    return True


# Returns all palindromes with length n from text
def get_palindromes(text, n):
    palindromes = []
    for i in range(0, len(text) - n):
        if is_palindrome(text[i:-(len(text) - (i + n))]):
            palindromes.append(text[i:-(len(text) - (i + n))])
    return palindromes


# txt = 'George Walker Bush (born July 6, 1946) is an American politician and businessman who served as the 43rd President of the United States from 2001 to 2009, and the 46th Governor of Texas from 1995 to 2000. The eldest son of Barbara and George H. W. Bush, he was born in New Haven, Connecticut. After graduating from Yale University in 1968 and Harvard Business School in 1975, Bush worked in oil businesses. He married Laura Welch in 1977 and ran unsuccessfully for the House of Representatives shortly thereafter. He later co-owned the Texas Rangers baseball team before defeating Ann Richards in the 1994 Texas gubernatorial election. Bush was elected president in 2000 after a close and controversial election, becoming the fourth president to be elected while receiving fewer popular votes nationwide than his opponent.[6] Bush is the second president to have been the son of a former president, the first having been John Quincy Adams.[7] He is also the brother of Jeb Bush, former Governor of Florida.'
# print get_palindromes(txt, 3)

x = [1, 2, 3, 7, 4, 5]
x.remove(7)
print(x)