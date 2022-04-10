def preprocess_docx(text):
    
    import re
    import string
    
    # 1. Lots of newlines, so split at the paragraph level
    text = text.split("\n")
    text = [string for string in text if string] # remove empty strings

    # 2. Remove small sentences & words
    bucket_new = []

    for sentence in text:
        word_list = sentence.strip().split()
        if len(word_list) > 5:                                  #remove 1- to 5-word 'sentences' (usually headings)
            sentence_new = ''
            for word in word_list:
                if len(word) > 1:                               #remove 1-char 'words'
                    sentence_new += (word + ' ')
            bucket_new.append(sentence_new.strip())

    bucket = [re.sub('/  +/g', ' ', sent) for sent in bucket_new] #condense whitespace to 1-space
    bucket = [string for string in bucket if string]              #remove empty strings
    
    # 3. Protect expressions of interest by renaming

    bucket = [sent.replace('i.e.', 'abbr-ie') for sent in bucket]
    bucket = [sent.replace('e.g.', 'abbr-eg') for sent in bucket]
    bucket = [sent.replace('et al.', 'abbr-etal') for sent in bucket]

    # 4. Process punctuation, numbers

    # Characters to replace with blank ''
    punc_to_blank = '!"#$%&\'()*+,<=>?@[\\]^_`{|}~:;.' + '“≥”≤±'  # retain hyphen - (important for compounds)
    # Characters to replace with space ' '
    punc_to_space = '‘’/'

    # Remove hyperlinks
    bucket = [re.sub(r"https?://\S+", "", text) for text in bucket]

    # Remove punctuation
    bucket = [re.sub('[%s]' % re.escape(punc_to_blank), '', text) for text in bucket]
    bucket = [re.sub('[%s]' % re.escape(punc_to_space), ' ', text) for text in bucket]

    # Remove numbers
    bucket = [re.sub('\w*\d\w*', '', text) for text in bucket]
    #bucket = [re.sub(r"\b[0-9]+\b\s*", "", text) for text in bucket]

    # Replace/remove punctuation requiring special treatment
    bucket = [sent.replace('–', ' - ') for sent in bucket] #en-dash
    bucket = [sent.replace('—', ' - ') for sent in bucket] #em-dash
    bucket = [sent.replace('\u3000', '') for sent in bucket] #headings
    bucket = [sent.replace('\t', '') for sent in bucket] #headings

    # 5. Remove small sentences & terms (repeats 2.)

    bucket_new = []

    for sentence in bucket:
        word_list = sentence.split()
        if len(word_list) > 5:                                  #remove 1- to 5-word 'sentences' (usually headings)
            sentence_new = ''
            for word in word_list:
                if len(word) > 4:                                #remove 1-char 'words'
                    if word[0] == '-':                           #remove leading hyphen
                        word = word[1:]
                    if word[-1] == '-':                          #remove trailing hyphen
                        word = word[:-1]
                    sentence_new += (word + ' ')
            bucket_new.append(sentence_new.strip())

    bucket = [re.sub('/  +/g', ' ', sent) for sent in bucket_new] #condense whitespace to 1-space
    bucket = [string for string in bucket if string]              #remove empty strings

    # 6. Combine sentences, paragraphs into one document

    document = ''

    for sentence in bucket:
        document += (sentence + ' ')

    document = re.sub('/  +/g', ' ', document.lower().strip()) #condense whitespace to 1-space

    return document