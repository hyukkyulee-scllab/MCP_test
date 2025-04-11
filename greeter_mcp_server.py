#!/usr/bin/env python

import sys
from fastmcp import FastMCP # Import the FastMCP class from the correct package

# Create an instance of the FastMCP server
# The name "simple-python-greeter" will be used to identify this server.
mcp_server = FastMCP(
    name="simple-python-greeter",
    version="0.1.0",
    description="A simple MCP server written in Python using fastmcp that provides a greeting tool."
)

# Define the 'greet' tool using the @mcp_server.tool() decorator
@mcp_server.tool()
def greet(name: str) -> str:
    """
    Generates a greeting message for the given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string like "Hello, [name]!".
    """
    if not isinstance(name, str) or not name:
        # You might want more robust error handling here
        return "Error: Please provide a valid name."
    return f"Hello, {name}!"

# Main execution block
if __name__ == '__main__':
    print("Starting simple-python-greeter MCP server...", file=sys.stderr)
    # Run the server - this will handle communication over stdio
    mcp_server.run()
    print("simple-python-greeter MCP server stopped.", file=sys.stderr)
