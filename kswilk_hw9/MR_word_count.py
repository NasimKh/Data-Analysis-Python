from mrjob.job import MRJob
from mrjob.step import MRStep
import re


WORD_RE = re.compile(r"(?:[^\w]*)(\w+)(?:[^\w]*)")

class MRWordCount(MRJob):
    def mapper(self, _, line):
        #Yield each word in the line
        for word in WORD_RE.findall(line):
            yield(word.lower(), 1)
    
    def combiner(self, word, counts):
        yield(word, sum(counts))
    
    def reducer(self, word, counts):
        yield (sum(counts),word)

if __name__ == '__main__':
    MRWordCount.run()