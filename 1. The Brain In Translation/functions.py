#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def collapse(text):
    
    """
    Paragraphs extracted from XML files contain different numbers of sentences,
    and even incomplete sentences. This function collapses a list of paragraphs
    into a list of sentences or sentence-equivalents in advance of NLP processing.
    """
    
    doc_raw = ""
    punc = set([".", ",", ";", ":"])
    for i, para in enumerate(text):
        if para[-1] in punc:
            doc_raw += (para + " ")
        else:
            doc_raw += (para + ". ")
        
    return doc_raw


# In[ ]:


def preprocess_gen(text):
    
    """
    This function is primarily for removing references, and fixing spacing
    between/within sentences in preparation for scispaCy language modeling.
    """
    
    import re
    
    text = text.replace('\u200a', '').replace('\n', '')   # remove weird space code, newlines
    text = re.sub('\[(\d+)\]', '', text)                  # remove refs ([1], [23], etc.)
    text = text.replace(' ,', '').replace(' .', '.')      # fix spaces created by prev line
    text = text.replace(' ;', ';').replace(' :', ':')     # 
    text = text.replace('  ', ' ')
    
    return text


# In[ ]:


def initialize_results_df():
    
    """
    Results DF should be reset for every hypothesis tested.
    Note: Run BEFORE preprocess_tok to capture unanalyzed tokens.
    """
    
    results_df = corpus_new[['Group', 'Author', 'Title']]
    results_df['Title'] = pd.Series([title[:31] for title in results_df['Title']])  # prune title for readability
    
    # with word count
    for i in range(0,20):
        # Pull text from df
        text = corpus_new.loc[i, "Text"]
        # Split by word (" " for simplicity)
        word_ct = len(text.split(' '))
        # Put in results_df
        results_df.loc[i, 'Word Count'] = word_ct
    
    return results_df


# In[ ]:


def unique(ls):
    
    """
    Creates a list of unique items from an existing list.
    """
 
    unique_list = []
     
    for x in ls:
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list


# In[ ]:


def preprocess_tok(doc):
    
    # Collect lemmas not tagged by spaCy as 1. punctuation, 2. digits, 3. URLs, or 4. stop words
    tokens = [tok.lemma_ for tok in doc if not (tok.is_punct | tok.is_digit | tok.like_url | tok.is_stop)]
    
    # Remove any tokens containing mid-string digits (e.g. "P5-a") or punc ('t(are')
    tokens = [tok for tok in tokens if not re.search("\d", tok)]
    tokens = [tok for tok in tokens if not re.search("\(", tok)]
    tokens = [tok for tok in tokens if not re.search("\)", tok)]
    
    # (4.13) Break apart hyphen- or slash-separated compounds
    seps = ['-', '–', '―',
            ';', ':',
            '\]', '\[', 
            '’', '”', 
            '>', '<', '/']
    for sep in seps:
        new_toks = []
        for tok in tokens:
            new_toks += tok.split(sep)
        tokens = new_toks
    
    # (4.13) Remove remaining abbreviations
    tokens = [tok for tok in tokens if not re.search("[a-zA-Z]\.[a-zA-Z]\.", tok)]
    tokens = [tok for tok in tokens if not re.search("\+", tok)]
    
    # Remove punc and small words (e.g. 'a', 'P', 'mm')
    punc_to_skip = set(['±', '=', '>', '<'])
    tokens = [tok for tok in tokens if tok not in punc_to_skip]     # can skip?
    tokens = [tok for tok in tokens if len(tok) > 3]    
       
    # Unify to lowercase (to simplify matching)
    tokens = [tok.lower() for tok in tokens]
    
    return tokens


# In[ ]:


def find_tokens_unique_to_one_doc(i):
    
    other_docs = list(range(0,20))
    other_docs.remove(i)
    
    # Doc in question
    text_i = corpus_new.loc[i, "Text"]
    doc_i = nlp(text_i)
    tokens_i = unique(preprocess_tok(doc_i))
    
    # Iterate thru all 19 other docs
    for j in other_docs:
        text_j = corpus_new.loc[j, "Text"]
        doc_j = nlp(text_j)
        tokens_j = set(unique(preprocess_tok(doc_j)))
        
        for tok in tokens_i:
            if tok in tokens_j:
                tokens_i.remove(tok)
    
    return tokens_i            


# In[ ]:


def lexeme_counter(doc, string):
    
    """
    Function for getting raw lemma count in a document.
    """
        
    tokens = preprocess_tok(doc)
    counter = 0
    for tok in tokens:
        if str(tok) == str(string):
            counter += 1
    
    return counter


# In[ ]:


def type_token_ratio(doc):
    
    token_list = preprocess_tok(doc)
    n_type = len(unique(token_list))
    n_token = len(token_list)
    ttr = n_type/n_token
    
    return ttr


# In[ ]:


def compare_means(var):
    
    from scipy.stats import ttest_ind
    
    jp_stats = list(results_df[results_df['Group'] == 'JP-EN'].loc[:, var])
    en_stats = list(results_df[results_df['Group'] == 'EN-EN'].loc[:, var])
    P = ttest_ind(jp_stats, en_stats).pvalue
    
    print(f'Mean {var}, JP-EN:  {np.mean(jp_stats)}')
    print(f'Mean {var}, EN-EN:  {np.mean(en_stats)}')
    print(f'Sig. (unpaired t-test): {P}')
    print('\n')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




