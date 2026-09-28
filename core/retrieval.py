from io import BytesIO
from pathlib import Path
from pypdf import PdfReader
def extract_upload(name,data):
    ext=Path(name).suffix.lower()
    if ext==".pdf":
        return "\n".join((p.extract_text() or "") for p in PdfReader(BytesIO(data)).pages)
    if ext in {".txt",".md",".csv",".json"}: return data.decode("utf-8",errors="replace")
    raise ValueError("Supported: PDF, TXT, MD, CSV, JSON")
