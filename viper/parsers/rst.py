from typing import List, Type

from docutils import parsers
from docutils.transforms import Transform, universal
import docutils.parsers.rst


from .parser import Parser


class RstParser(Parser, parsers.rst.Parser):
    def get_transforms(self) -> List[Type[Transform]]:
        transforms = super().get_transforms()
        transforms.remove(universal.SmartQuotes)
        return transforms

    def parse(self, inputstring, a=None):
        components = (docutils.parsers.rst.Parser,)
        settings = docutils.frontend.OptionParser(
            components=components
        ).get_default_values()
        document = docutils.utils.new_document('<rst-doc>', settings=settings)
        super(Parser, self).parse(inputstring, document)
        return document
