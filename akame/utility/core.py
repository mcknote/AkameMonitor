import logging
from datetime import datetime
from typing import Any, Optional, Hashable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MonitoredContent:
    """Class that structures monitored content

    Args:
        content (Union[Any, None], optional):
            Any monitored content. Defaults to None.
    """

    def __init__(self, content: Optional[Any] = None):
        self.content = content
        self.timestamp = datetime.now()
        logger.info(f"Initiated {self.__class__.__name__} at {self.timestamp}")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(timestamp={self.timestamp.__repr__()}, "
            f"content={self.content.__repr__()})"
        )

    def __key(self) -> Hashable:
        """Function that defines the key of a monitored content

        Returns:
            Hashable: Hashable object
        """
        if isinstance(self.content, Hashable):
            content_key = self.content
        else:
            content_type = type(self.content)
            try:
                logger.warning(
                    f"Content type {content_type} is not hashable. "
                    "Trying to convert it to tuple"
                )
                content_key = tuple(self.content)
            except TypeError:
                logger.warning(
                    f"Content type {content_type} cannot be converted "
                    "to tuple. Trying to use the content's __repr__. "
                    "Consider changing the monitored content as "
                    "this may result in falsy comparison"
                )
                content_key = repr(self.content)

        return content_key

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, other):
        if isinstance(other, MonitoredContent):
            return self.__key() == other.__key()
        return NotImplemented