# Load Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import os

sum_path = "../../submissions"
trans_path = "../../Transcript"

import nltk
nltk.download('punkt')


Transcripts = {}
for file in os.listdir(trans_path):
  if ".txt" in file:
    Transcripts[file] = PlaintextParser.from_file("{}/{}".format(trans_path,file),Tokenizer("english"))

from sumy.summarizers.text_rank import TextRankSummarizer

if "TextRank" not in os.listdir(sum_path):
  os.mkdir("{}/TextRank".sum_path)

txtRank = TextRankSummarizer()


for key,value in Transcripts.items():
  summaries = txtRank(value.document,50)

  final_summary = ""
  for sent in summaries:
    final_summary += str(sent) + "\n"
  open("{}/TextRank/{}".format(sum_path,key),"w",encoding="utf-8").write(final_summary)
