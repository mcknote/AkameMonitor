import logging
from typing import Any, Union

from .core import ComparerBase
from .formatter import StringDelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasicComparer(ComparerBase):
    """Class that defines the basic comparer"""

    def __init__(self) -> None:
        logging.info(f"Initializing comparer: {self.__class__.__name__}")

        self.comparison_status: Union[bool, None] = None
        self.status_code: int = -1
        self.message: str = ""

    def load_comparison_status(self) -> None:
        if self.content_0 is None:
            self.comparison_status = None
        else:
            self.comparison_status = self.content_0 != self.content_1

    def get_delta_plain_text(self):
        finder = StringDelta(a=self.content_0, b=self.content_1)
        return finder.get_delta_in_colored_terminal_text()

    def express_comparison_results(self) -> None:
        if self.comparison_status is None:
            self.status_code = -1
            self.message = "INITIATED"
        elif not self.comparison_status:
            self.status_code = 0
            self.message = "UNCHANGED"
        else:
            self.status_code = 1
            message_header = "CHANGES DETECTED"
            message_changes = self.get_delta_plain_text()
            self.message = f"{message_header}\n{message_changes}"

    def main(self, content_0: Any, content_1: Any) -> None:
        self.content_0 = content_0
        self.content_1 = content_1
        self.load_comparison_status()
        self.express_comparison_results()
