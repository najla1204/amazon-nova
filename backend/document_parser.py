class DocumentParser:
    """
    Handles OCR and data extraction from document images.
    """
    def __init__(self):
        # Keep NovaClient initialized for future integration
        from nova_client import NovaClient
        self.nova = NovaClient()

    async def parse_document(self, image_bytes: bytes, filename: str = ""):
        """
        Simulates structured information extraction from a document image.
        Uses rule-based logic for now.
        """
        filename_lower = filename.lower()
        
        if "bill" in filename_lower:
            return {
                "document_type": "electricity_bill",
                "name": "Ravi Kumar",
                "account_number": "987654321",
                "address": "Chennai"
            }
        
        # Generic fallback
        return {
            "document_type": "unknown",
            "extracted_data": "Generic document data detected",
            "filename": filename
        }
