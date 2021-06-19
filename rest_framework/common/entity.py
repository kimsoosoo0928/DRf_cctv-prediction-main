from dataclasses import dataclass

@dataclass
class FileDTO(object):

    context: str
    fname: str
    dframe: object


    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def context(self, fname):
        self.fname = fname

    @property
    def dframe(self) -> str: return self.dframe

    @dframe.setter




    def context(self, dframe):
        self.dframe = dframe