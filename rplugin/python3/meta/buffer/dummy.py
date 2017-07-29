
from .buffer import AbstractBuffer


class DummyBuffer(AbstractBuffer):
  """A vim buffer not meant for end consumption, but as a malleable and
  temporary mirror"""
  name = 'dummy'


    def __init__(self, buffer):
        """Constructor.

        Args:
            nvim.buffer (neovim.Nvim): A ``neovim.Nvim.buffer`` instance.
        """
        self.vimbuffer = buffer   # the nvim.buffer object holding our results
        self.sources = []         # a list of Buffer objects, together
        # representing the total text content of this dummy buffer
        # self.matcher/s
        self.attributes = {[]}    # the relevant optialso reachable from the buffer object itself..ons we need, also
        self.ranker = ranker # steal something from denite since we need to be able to
        # sort, not the text within each source but the sources themselves
        # self.syntax = if created from one source/all sources same syntax then
        # use it automatically. 
        self.presentation = False        #like for dummy buffers, stuff to change
        # presentation (whitespace, columns etc...) and other minor stuff,
        # without touching original for those operations

    def idea(self, hmm)
    """what if we just make everything fully abstract and so everything is just
    a stack of operations. Or I mean we should keep better structure over stuff
    but ALSO keep something like that so that every single contribution (extra
    text, text filtered out, text edited...) can be taken out/changed or
    whatever, after the fact. Obvs would break or run against what we actually
    want, a lot, but can prob squeeze something p cool out of what does work.

    Oh and fucking hell are we involving text objects wrt filtering!! So here,
    write "def", and that'll mean all the lines in the current file with
    function definitions on them. Stack on some more individual files, or cmd
    like "all py files in folder", and a textobj filter, then cycle from like
    just lines with func defs, to all function bodies, etc"""


    def add(self, buffer)
    """Add/connect a Buffer source to the dummy buffer"""

    def text(self, text, matcher)
    """Get the full text representing the sources"""

    def filter(self, matcher)   # look closer at lista's filters and how fzr/denite etc do it.
    """Apply a semi-permanent filter limiting the contents in turn presented to
    matchers and available for modification"""

    def freeze(self, matcher)
    """Match text, but instead of hiding it, make it immutable/not propogate
    back to its originating buffer (+ i guess, when fucked with, restore it
    either immediately or like with some autocmd timeoutlen)
    """
