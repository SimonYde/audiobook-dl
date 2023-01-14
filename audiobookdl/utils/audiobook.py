import requests
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class AudiobookFile:
    # Url to audio file
    url: str
    # Output file extension
    ext: str
    # Title of file
    title: Optional[str] = None
    # Headers for request
    headers: Dict[str, str] = field(default_factory=dict)
    # AES decryption key
    encryption_key: Optional[bytes] = None
    # AES initialization vector
    iv: Optional[bytes] = None


class AudiobookMetadata:
    title: str
    _authors: List[str]
    _narrators: List[str]

    @property
    def authors(self) -> str:
        return "; ".join(self._authors)

    @property
    def narrators(self) -> str:
        return "; ".join(self._narrators)

class Audiobook:
    _session: requests.Session
    metadata: AudiobookMetadata
    files: List[AudiobookFile]
    cover: Optional[bytes]
    cover_extension: str

    @property
    def title(self) -> str:
        return self.metadata.title