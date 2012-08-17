from mincepie import mapreducer, launcher

class WordCountMapper(mapreducer.BasicMapper):
    def map(self, k, v):
        for word in v.split():
            yield word, 1

mapreducer.REGISTER_MAPPER(WordCountMapper)


class WordCountReducer(mapreducer.BasicReducer):
    def reduce(self, k, v):
        return sum(v)

mapreducer.REGISTER_REDUCER(WordCountReducer)


class ZenReader(mapreducer.BasicReader):
    """A demo reader that reads the zen of python
    """
    def read(self, inputlist):
        zen = ["Beautiful is better than ugly",
               "Explicit is better than implicit",
               "Simple is better than complex",
               "Complex is better than complicated",
               "Flat is better than nested",
               "Sparse is better than dense",
               "Readability counts",
               "Special cases aren't special enough to break the rules",
               "Although practicality beats purity",
               "Errors should never pass silently",
               "Unless explicitly silenced",
               "In the face of ambiguity, refuse the temptation to guess",
               "There should be one-- and preferably only one --obvious way to do it",
               "Although that way may not be obvious at first unless you're Dutch",
               "Now is better than never",
               "Although never is often better than *right* now",
               "If the implementation is hard to explain, it's a bad idea",
               "If the implementation is easy to explain, it may be a good idea",
               "Namespaces are one honking great idea -- let's do more of those!"
              ]
        return dict(enumerate(zen))

mapreducer.REGISTER_READER(ZenReader)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    launcher.launch_mpi()

