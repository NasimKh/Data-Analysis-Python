from mrjob.job import MRJob
from mrjob.step import MRStep


class MRsummarystats(MRJob):
    
    def steps(self):
        return[
            MRStep(mapper=self.mapper_get_pairs,
                   reducer = self.reducer_count_key),
            MRStep(reducer = self.reducer_var_key)
        ]
    
    ##Get pairs out of file
    def mapper_get_pairs(self, _, line):

        key, value = line.split('\t')
        cnt = 1
        value = float(value)
        yield key, (value, cnt)
        
    
    ##Get count of keys and mean
    # Mean = sum(x)/n
    def reducer_count_key(self, key, values):
        key_count = 0
        val_sum = 0
        vals = []
        for value, cnt in values:
            val_sum += value
            key_count += 1
            vals.append(value)
        
        yield key, (key_count, (val_sum/key_count), vals)
        
    
    #get variance
    # variance (x-mean)^2 / (n-1)
    def reducer_var_key(self, key, values):
        var = 0
        for cnt, mn, val in values:
            for i in val:
                var += ((i-mn)**2)
               
        yield key, (cnt, mn, (var/(cnt-1)))

     

if __name__ == '__main__':
    MRsummarystats.run()