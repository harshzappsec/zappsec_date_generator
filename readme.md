```markdown
# Device Support Date Generator

A toolset for retrieving hardware/software support dates from official sources using different AI approaches.

## Features
- Two implementations available:
  1. `date_generator_openai.py` - Direct OpenAI API implementation
  2. `date_generator_using_agentic_ai.py` - Agentic AI implementation with search capabilities
- Returns structured JSON with official reference links
- Handles both hardware and software lifecycle dates

## Installation

```bash
# Clone repository
git clone https://github.com/your-org/device-support-date-generator.git
cd device-support-date-generator

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY='your-api-key-here'

Usage
OpenAI Direct Implementation
python date_generator_openai.py

Agentic AI Implementation
python date_generator_using_agentic_ai.py


Configuration
# Required for both implementations
OPENAI_API_KEY=your-openai-api-key

# Optional for Agentic version (if using Google Search)
GOOGLE_API_KEY=your-google-api-key


Example Output
{
  "Last Date of Support for HW": {
    "date": "2024-12-31",
    "reference": "https://manufacturer.com/support/3850"
  },
  "Last Date of Security Support for SW": {
    "date": "2025-06-30",
    "reference": "https://manufacturer.com/security-updates"
  }
}

Dependencies
    Python 3.10
    OpenAI Python client
    agno framework (for agentic version)
    Google Search API (for agentic version)

Implementation Details
    date_generator_openai.py
    Direct GPT-4 completion with JSON response format
    Single API call implementation
    Basic error handling

    date_generator_using_agentic_ai.py
    Agentic workflow with automated source verification
    Google Search integration for fact-checking
    JSON response validation and extraction
    Advanced error recovery patterns

Limitations
    Accuracy depends on available online documentation
    Requires internet connection for search functionality
    Rate limits may apply for API services