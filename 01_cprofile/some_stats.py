import pstats
from pstats import SortKey

# Run the following in the command line
# python -m cProfile -o <output_file> <file_to_profile>
# e.g.
# python -m cProfile -o profile.stats 01_cprofile/corrector.py

p = pstats.Stats("profile.stats")
p.strip_dirs().sort_stats(SortKey.TIME).print_stats(10)
# p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(10)
