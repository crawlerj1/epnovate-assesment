from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.decorator import tool
from agno.tools.file.generation import FileGenerationTools


@tool
def get_market_benchmark():
    """This Tool is reqistered for the Checking up the benchmark for """
    return "Tool is Registered";

@tool
def check_compliance_risks():
    """This Tool is reqistered for Checking up the Compliance Risk"""
    return "Tool is Registered";

@tool
def web_search(url,search_query):
    """User This tool to scrap the webnews """
    myscraper=Crawl4aiTools(max_length=5000)
    return myscraper.crawl(url=url,search_query=search_query)
@tool
def generate_pdf():
    """This tool is used to generate the PDF of connect"""
    return FileGenerationTools.generate_pdf_file