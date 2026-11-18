
from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.decorator import tool
from agno.tools.file_generation import FileGenerationTools


@tool
def web_search(url: str, search_query: str = "") -> str:
    """Scrape news content from the given URL.
    Args:
        url: Website or article URL to scrape.
        search_query: Topic to focus on.
    """
    myscraper = Crawl4aiTools(max_length=5000)

    result = myscraper.crawl(
        url=url,
        search_query=search_query
    )

    return result


@tool
def generate_pdf(
    content: str,
    filename: str = "market_report.pdf",
    title: str = "Market Research Report"
) -> str:
    """
    Generate and save a PDF report.

    Args:
        content: Full report content.
        filename: Output PDF filename.
        title: Title of the report.
    """
    pdf_tool = FileGenerationTools(
        output_directory="reports"
    )

    result = pdf_tool.generate_pdf_file(
        content=content,
        filename=filename,
        title=title
    )

    return result.content
