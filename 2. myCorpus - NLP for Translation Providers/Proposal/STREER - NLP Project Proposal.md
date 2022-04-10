## Module #5 Project Proposal
### Mark Streer (DS/ML)

#### Question / Need:
Globally, scientific literature is disseminated in English, yet the language is spoken by fewer than 20% of the world's population, and only 5% speak it natively. Researchers working in non-Anglophone countries normally enlist help from translators and/or editors (or firms which employ them) when publishing in a second language, but this approach incurs additional costs (human labor). Google Translate, Microsoft Translator, and other machine translation (MT) services have made decent-quality general translation engines available for free, but the precision required of technical translation typically requires some human intervention to edit the output, known as 'post-MT editing'. Still, editors and translators are inconsistent in their edits and diction. Could biomedical corpora be used to better educate them on expected genre-specific language?

Translators are expected not only to know the meaning of a source text, but also to know the language conventionally used to express that meaning in the target language. For example, to translate the Spanish 'Yo tengo hambre', an English speaker must know not only each word's meaning ("I", "Have", "Hunger"), but that the concept is naturally expressed in English using the verb 'to be' with the corresponding adjective: "I am hungry". Genre conventions can be conceptualized in terms of expected frequencies and positions of different lexemes/morphemes; direct replication in the target language of such linguistic features from the source language seldom produces the most coherent, cohesive, or comprehensible result. 

#### Data Description:

In this project, I will explore a personal dataset: a collection of my technical translations from Japanese to English over the last six years. The genres of these documents are generally research article (RA) in IMRAD format and/or abstract (Abs). There are roughly 1000 documents in total, but processing from DOCX format is taking considerable time: if need be, documents will be split by paragraphs to obtain sufficient data. Neuroscience, nursing, gerontology, clinical trials, and civil engineering are among the domains expected to be most broadly represented in this corpus (if memory serves).

The prose of a single translator is hardly representative: scientific corpora are normally drawn from a wide variety of sources and authors. Still, the rules applied to distill technical Japanese from diverse authors and domains should be relatively **consistent** within any given translator (i.e. my writing style). 

The specific business use case is my own, as I am curious to know:
* Does my own technical English writing exhibit linguistic features of technical Japanese? That is, if I compared my translations with de novo English - i.e., as written by L1 English authors - would certain vocabulary, grammatical structures, or other features indicate their Japanese origin?  
* Do these characteristics persist across different domains? Are some domain-specific?
* Can such differentials be framed to teach L2 English writers how to write technical English expected of their specific audience/genre? L1 English writers?

#### Tools:

1. textextract: Extract text from .docx files and import into Python
2. spaCy+ScispaCy: NLP operations

#### MVP Goal:
* Topic modeling for as many documents as I can import by next Monday.