from agno.agent.agent import Agent
from agno.models.groq import Groq
from tools import (check_compliance_risks, generate_pdf, get_market_benchmark,
                   web_search)


def llmCall():

    result=Agent(
        model=Groq(id= "openai/gpt-oss-120b",api_key=""),
        instructions="This is LLM Call for the Market Benchmark Check and Compliance Check and generate PDF in accordance",
        tools=[get_market_benchmark,check_compliance_risks,web_search,generate_pdf],
        debug_mode=True
    )
    output=result._response(input="Fetch Fresh News Article from the webscraper/websearch tool , get market benchmark and generate PDF, use this  https://www.ndtv.com/ for websearch")
    return output;