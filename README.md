# AI Agent with Multi-Source Querying and Tool Integration

This project is an AI-powered agent capable of handling both structured (CSV) and unstructured (PDF) data sources using LlamaIndex. The agent dynamically selects the appropriate data source or tool to answer complex questions and perform various tasks, including note-taking.

***Agent Workflow***
1. **Data Source Initialization**: Loads structured data (CSV) using Pandas and unstructured data (PDF) using LlamaIndex readers.
2. **Query Engine Creation**: Sets up query engines for each data source. The Pandas query engine is used for structured data, and a vector store index is used for unstructured data.
3. **Tool Integration**: Custom tools, such as the note-taking tool, are added to extend the agent’s capabilities.
4. **Query Handling**: The agent selects the appropriate query engine or tool based on the context and user query, allowing it to pull information from the correct source.
