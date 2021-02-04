import logging
from typing import Any, TypeVar, Union

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# define types
ComparerType = TypeVar("ComparerType", bound="ComparerBase")


class ComparerBase:
    """Class that defines the base comparer"""

    def __init__(self) -> None:
        logging.info(f"Initializing comparer: {self.__class__.__name__}")
        self.comparison_status: Union[bool, None] = None
        self.status_code: int = -1
        self.message: str = ""

    def load_comparison_status(self) -> None:
        pass

    def express_comparison_results(self) -> None:
        pass

    def main(self, content_0: Any, content_1: Any):
        """Function that loads the content to compare

        Args:
            content_0 (Any): Archived monitored content or predefined
                constants to be compared against
            content_1 (Any): Current mnoitored content
        """
        self.content_0 = content_0
        self.content_1 = content_1
        pass
