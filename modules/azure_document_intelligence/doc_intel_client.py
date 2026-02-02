from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError


class DocIntelClient:
    def __init__(self, endpoint: str):
        """
        Initializes the client using DefaultAzureCredential.
        :param endpoint: The 'Document Intelligence' endpoint from your Foundry project.
        """
        self.client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=DefaultAzureCredential()
        )

    def analyze_layout(self, file_path: str = None, doc_url: str = None) -> AnalyzeResult:
        """
        Uses the 'prebuilt-layout' model to extract text, tables, and selection marks.
        """
        try:
            if doc_url:
                poller = self.client.begin_analyze_document(
                    "prebuilt-layout",
                    AnalyzeDocumentRequest(url_source=doc_url)
                )
            elif file_path:
                with open(file_path, "rb") as f:
                    poller = self.client.begin_analyze_document(
                        "prebuilt-layout",
                        body=f,
                        content_type="application/octet-stream"
                    )
            else:
                raise ValueError("You must provide either a file_path or a doc_url.")

            return poller.result()

        except HttpResponseError as e:
            print(f"Analysis failed: {e}")
            raise

    def print_summary(self, result: AnalyzeResult):
        """Helper to print out the core findings."""
        print(f"--- Analysis Summary ---")
        print(f"Detected {len(result.pages)} pages.")

        # Extract all text lines
        for page in result.pages:
            print(f"Page {page.page_number} has {len(page.lines)} lines of text.")

        # Extract table info
        if result.tables:
            for i, table in enumerate(result.tables):
                print(f"Table {i} found with {table.row_count} rows and {table.column_count} columns.")

    def get_full_text(self, result: AnalyzeResult):
        output = []
        for page in result.pages:
            print(f"--- Extracting Page {page.page_number} ---")
            for line in page.lines:
                output.append(line.content)

        return "\n".join(output)