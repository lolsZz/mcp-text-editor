#!/usr/bin/env python3
"""Entry point script for the MCP text editor server."""

import asyncio
from mcp_text_editor.server import main

if __name__ == "__main__":
    asyncio.run(main())
