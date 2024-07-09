import os

import line_profiler

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
GATSBY_TXT = os.path.join(SCRIPT_DIR, "gatsby.txt")


# By default this will do nothing and not slow down the code, it needs to be enabled by:
# LINE_PROFILE=1 pytest 02_line_profile/count_words.py
# or
# LINE_PROFILE=1 python 02_line_profile/count_words.py
# in the command line
@line_profiler.profile
def count_words(filename):
    # Tried with counter, and default dict but they are slower than this
    word_counts = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
    return word_counts


def test_count_words(benchmark):
    result = benchmark(count_words, GATSBY_TXT)


if __name__ == "__main__":
    count_words(GATSBY_TXT)
