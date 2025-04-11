# Simple Python MCP Greeter Server (using fastmcp)

This project contains a simple Model Context Protocol (MCP) server written in Python using the `fastmcp` library. It provides a single tool to generate greetings.

## Files

*   **`greeter_mcp_server.py`**: The main Python script for the MCP server. It uses `fastmcp` to define and run the server.
*   **`.venv` (directory)**: A Python virtual environment (likely created by Pycharm) where dependencies like `fastmcp` are installed.

## Functionality

The server provides one tool:

*   **`greet`**:
    *   **Description**: Generates a greeting message for the given name.
    *   **Input**: A JSON object with a required `name` property (string). Example: `{ "name": "World" }`
    *   **Output**: A string like "Hello, \[name]!".

## Prerequisites

1.  **Python**: Ensure Python is installed.
2.  **fastmcp**: The `fastmcp` library and its dependencies must be installed in the Python environment that will run the server. If using the `.venv` directory within this project, you likely installed it by running `pip install fastmcp` while the virtual environment was active.

## Configuration with Cline

To make this server available to Cline, you need to add its configuration to Cline's MCP settings file.

1.  **Locate the settings file**: Typically found at `C:\Users\<YourUsername>\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`.
2.  **Add the server configuration**: Edit the JSON file and add an entry for `simple-python-greeter` within the `mcpServers` object. **Crucially, ensure the `command` points to the Python executable *inside* the virtual environment where `fastmcp` is installed.**

    ```json
    {
      "mcpServers": {
        // ... other servers might be listed here ...

        "simple-python-greeter": {
          // IMPORTANT: The path below depends on your specific project location and virtual environment setup.
          // Adjust it to point to the 'python.exe' (Windows) or 'python' (macOS/Linux)
          // inside your project's virtual environment script directory (e.g., .venv/Scripts or .venv/bin).
          "command": "c:/Users/<YourUsername>/PycharmProjects/MCP_test/.venv/Scripts/python.exe",
          "args": [
            // This path also depends on your project location.
            "c:/Users/<YourUsername>/PycharmProjects/MCP_test/greeter_mcp_server.py"
          ],
          "disabled": false, // Set to false to enable
          "autoApprove": [],
          "transportType": "stdio",
          "timeout": 60
        }
      }
    }
    ```

3.  **Restart/Reload Cline**: Cline should automatically detect the changes and attempt to start the server.

## Using the Server with Cline

Once the server is configured and running (you should see `simple-python-greeter` listed under "Connected MCP Servers" in Cline's system prompt), you can ask Cline to use its tool:

*   Example prompt for Cline: `"Use the simple-python-greeter server to greet 'Middle Schooler'"`

Cline will then use the `use_mcp_tool` capability internally to call the `greet` tool on your running Python server.
