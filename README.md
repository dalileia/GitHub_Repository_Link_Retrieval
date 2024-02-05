GitHub Repository Link Retrieval

This Python code retrieves links of GitHub repositories based on the provided search criteria. It offers flexibility in searching by a phrase or word, and optionally by start and finish dates.

Features
Phrase Search: You can search for repositories based on a phrase or word. If only a phrase is provided, it will return a maximum of 1000 results.

Date Range Search: You can specify a start and finish date to search for repositories created within that date range. If a finish date is not provided, it defaults to today's date.

Daily Search: When providing a start and finish date, the code will search for repositories each day within the specified range to ensure all relevant repositories are captured.

JSON Output: The retrieved repository links are stored in a JSON file for easy consumption and analysis.

Output:
The retrieved GitHub repository links will be stored in a file named github_search.json in the current directory.