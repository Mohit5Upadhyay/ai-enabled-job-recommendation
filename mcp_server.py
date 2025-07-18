from mcp.server.fastmcp import FastMCP  # pip install mcp[cli]
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs 

# initialize FastMCP server
mcp = FastMCP("Job Recommender")

@mcp.tool()
async def fetchlinkedin(listofkey):
    return fetch_linkedin_jobs(listofkey)

@mcp.tool()
async def fetchnaukri(listofkey):
    return fetch_naukri_jobs(listofkey)


if __name__ == "__main__":
    mcp.run(transport='stdio')


# testing server: 
# - mcp dev mcp_server.py  ==> inspect the server
