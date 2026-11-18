import asyncio
import sys
from pathlib import Path

from agno.agent.agent import Agent
from agno.models.groq import Groq
from agno.tools.mcp import MCPTools
from tools import generate_pdf, web_search


def llmCall():

    server_path = Path(__file__).with_name("mcp_server.py")
    mcp_tools = MCPTools(
        command=f'"{sys.executable}" "{server_path}"'
    )

    result=Agent(
        model=Groq(id= "openai/gpt-oss-120b"),
        instructions="This is LLM Call for the Market Benchmark Check and Compliance Check of enterprise (use mcp for it) with correspondence to Internet Latest News with respect to the topic and  generate PDF in accordance",
        tools=[mcp_tools,web_search,generate_pdf],
        debug_mode=True
    )
    response = asyncio.run(
        result.arun(
            "Research AI adoption in banking. "
            "Use https://www.ndtv.com/ as a news source. "
            "Retrieve market benchmarks and compliance risks "
            "through MCP and generate a PDF report."
        )
    )

    return response