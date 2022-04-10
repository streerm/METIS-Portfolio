## Module #4 Project Proposal
### Mark Streer (DS/ML)

#### Question / Need:
Speech processing is an important domain of artificial intelligence essential to speech transcription, virtual assistant commands, and speaker identification. Several teams have attempted to determine speaker identity (speaker diarization), accents, and even emotions based on features engineered from speech waveforms. This project aims to classify accents using a series of classification models, compare their performances, and identify which features contribute most predictive value.

The business case is accent recognition broadly. For example, lots of voice recognition software has been trained on samples from native-speaking, homogeneous speaker groups, so they perform poorly on speakers who are not from the same sociolinguistic background. Comparable models could be trained on non-native English speech: one model for L2 speakers from Mexico, a different model for L2 speakers from China, etc. During an automated customer service or touchtone interaction, if the caller's accent could be identified promptly, they could be funneled into the specialized model to receive further commands more accurately.

#### Data Description:

The dataset contains crowdsourced yet high-quality audio recordings of native English speakers of both sexes from different parts of the British Isles, and was originally published by [Google Research](https://aclanthology.org/2020.lrec-1.804.pdf).
Raw audio data and label counts can be found on [OpenSLR.org](https://www.openslr.org/83/).

Dialect labels are: Southern England, Midlands, Northern England, Welsh English, Scottish English and Irish English.

I plan to derive two kinds of features from the raw audio data:  
1. Mel-frequency cepstrum coefficients (MFCCs) using [openSMILE 3.0](https://www.audeering.com/research/opensmile/), or alternatively [Librosa](https://librosa.org/doc/main/generated/librosa.feature.mfcc.html).  
2. Phonemic transcriptions using [CMUSphinx](https://cmusphinx.github.io/wiki/phonemerecognition/). Although the accuracy is hardly perfect, identifying phonemes more common in certain regions than others - especially vowels - 

#### Tools:

1. [openSMILE 3.0](https://audeering.github.io/opensmile/about.html#audio-features-low-level). 
2. [CMUSphinx](https://cmusphinx.github.io/wiki/phonemerecognition/)
    [Tutorial & code for phonemic transcription](https://stackoverflow.com/questions/30705028/convert-sound-to-list-of-phonemes-in-python)
    [UK English phonemic dictionary](https://www.keithv.com/software/sphinx/uk/)

#### MVP Goal:
* Performance metrics for three classification models:
1. Logistic regression
2. K nearest neighbors
3. ?
* Confusion matrix (heatmaps)
* Precision, recall, PPV, NPV


### Template

#### Question/need:
* *What is the framing question of your analysis, or the purpose of the model/system you plan to build?* 
* *Who benefits from exploring this question or building this model/system?*

#### Data Description:
* *What dataset(s) do you plan to use, and how will you obtain the data?*
* *What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?* 
* *If modeling, what will you predict as your target?*

#### Tools:
* *How do you intend to meet the tools requirement of the project?* 
* *Are you planning in advance to need or use additional tools beyond those required?*

#### MVP Goal:
* *What would a [minimum viable product (MVP)](./mvp.md) look like for this project?*


