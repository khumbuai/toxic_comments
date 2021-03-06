UNKNOWN_WORD = "_UNK_"
END_WORD = "_END_"
NAN_WORD = "_NAN_"
COMMENT = "comment_text"
LIST_CLASSES = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
MODELS_FP = 'models/'
TRAIN_FILENAME = 'assets/raw_data/train.csv'
TRAIN_FILENAME_FR = 'assets/raw_data/train_fr.csv'
TEST_FILENAME = 'assets/raw_data/test.csv'
LIST_LOGITS = ['logits_' + c for c in LIST_CLASSES]
TRAIN_SLIM_FILENAME = 'assets/raw_data/train_slim.csv'
VALID_SLIM_FILENAME = 'assets/raw_data/valid_slim.csv'
SAMPLE_SUBMISSION_FILENAME = 'assets/raw_data/sample_submission.csv'
UNKNOWN_CHAR = 'ⓤ'
PAD_CHAR = '℗'