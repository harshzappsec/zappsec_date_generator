# Device Support Date Generator

A toolset for retrieving hardware/software support dates from official sources using different AI approaches.

## Features
- Two implementations available:
  1. **`date_generator_openai.py`** - Direct OpenAI API implementation
  2. **`date_generator_using_agentic_ai.py`** - Agentic AI implementation with search capabilities
- Returns structured JSON with official reference links
- Handles both hardware and software lifecycle dates

## Installation

```bash
# Clone repository
git clone https://github.com/harshzappsec/zappsec_date_generator.git
cd zappsec_date_generator

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### OpenAI Direct Implementation
```bash
python date_generator_openai.py
```

### Agentic AI Implementation
```bash
python date_generator_using_agentic_ai.py
```

## Configuration

### Required for both implementations
```bash
OPENAI_API_KEY=your-openai-api-key
```

### Optional for Agentic version (if using Google Search)
```bash
GOOGLE_API_KEY=your-google-api-key
```

## Example Output
```json
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
```

## Dependencies
- Python 3.10
- OpenAI Python client
- `agno` framework (for Agentic version)
- Google Search API (for Agentic version)

## Implementation Details

### `date_generator_openai.py`
- Direct GPT-4 completion with JSON response format
- Single API call implementation
- Basic error handling

### `date_generator_using_agentic_ai.py`
- Agentic workflow with automated source verification
- Google Search integration for fact-checking
- JSON response validation and extraction
- Advanced error recovery patterns