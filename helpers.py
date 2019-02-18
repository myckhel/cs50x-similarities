from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    # split the strings with new line
    astr = a.split('\n')
    bstr = b.split('\n')
    # declare empty set for adding similarity
    similarities = set()
    # check for similarities between two lines
    # add to similarities set
    # for length of first lines times
    for i in range(len(astr)):
        if astr[i] in bstr:
            similarities.add(astr[i])
    # similarities to list and return
    return list(similarities)


def sentences(a, b):
    """Return sentences in both a and b"""
    # TODO
    # split the strings into list sentences
    asen = sent_tokenize(a)
    bsen = sent_tokenize(b)
    # declare empty set for adding similarity
    similarities = set()
    # check for similarities between two sentences
    # add to similarities set
    # do for minimum sentences list length
    for i in range(len(asen)):
        if asen[i] in bsen:
            similarities.add(asen[i])
    # similarities to list and return
    return list(similarities)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    # define a function
    # that return the list of possible substring of length
    def subStrs(string, length):
        strings = set()
        end = True
        stringLength = len(string)
        start = 0
        # for i in range(len(string) - 1):
        while end:
            stop = start + length
            if stop > stringLength:
                end = False
                continue
            strings.add(string[start: stop])
            start = start + 1
        return list(strings)
    # get the list of possible substring
    astr = subStrs(a, n)
    bstr = subStrs(b, n)
    # declare empty set for adding similarity
    similarities = set()
    # check for similarities between two possible substring list
    # add to similarities set
    for i in range(len(astr)):
        if astr[i] in bstr:
            similarities.add(astr[i])
    # similarities to list and return
    return list(similarities)
