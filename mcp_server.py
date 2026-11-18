from fastmcp import FastMCP

mcp=FastMCP("Company's Data")
@mcp.tool()
def get_market_benchmarks(topic: str) -> dict:
    """This Tool is reqistered for the Checking up the benchmark for company"""

    return {
        "topic": topic,
        "source": "db",
        "metrics": {
            "adoption_rate": 42,
        }
    }


@mcp.tool()
def check_compliance_risks(topic: str) -> dict:
    """this Tool is reqistered for Checking up the Compliance Risk"""

    return {
        "topic": topic,
        "source": "db",
        "risks": [
            "Data privacy compliance review",
            "Sensitive information handling",

        ]
    }

if __name__ == "__main__":
    mcp.run()
