 This is a  Python script used to prepare raw documents so an AI model can search and reference them.

• Document Loading. Reads raw external files (such as PDFs, Word docs, Markdown, or web pages) using tools like PyPDF2, LangChain, or LlamaIndex.
• Text Cleaning. Removes unnecessary formatting, headers, footers, or extra whitespace so the text is clean and consistent.
• Chunking (Text Splitting). Breaks large documents into smaller, overlapping pieces (e.g., 500–1,000 characters) so they fit within an AI model's context limits and preserve meaning across boundaries.
