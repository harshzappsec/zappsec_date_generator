from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
import json
import os
import re

def extract_json_from_response(response_text):
    # Find JSON content between triple backticks
    json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
    if json_match:
        return json_match.group(1)
    
    # If no triple backticks, try to find content between curly braces
    json_match = re.search(r'(\{.*\})', response_text, re.DOTALL)
    if json_match:
        return json_match.group(1)
    
    return response_text

def get_device_support_dates(device_name):
    agent = Agent(
        model=OpenAIChat(id="gpt-4o", temperature=0.3, api_key=os.environ["OPENAI_API_KEY"]),
        description="You are a technical expert specialized in IT hardware and software lifecycle management.",
        instructions=[
            "1. Search Strategy:",
            "   - Search using the exact device name/model/PID without modifications",
            "   - First identify the manufacturer from the device name",
            "   - Focus on official manufacturer documentation, especially End-of-Life notices",
            "   - Search manufacturer support sites, product bulletins, and lifecycle pages",
            
            "2. Device Verification:",
            "   - Verify the exact model/product match in search results",
            "   - Exclude results for different variants unless specifically mentioned",
            "   - For hardware bundles, focus on the main component's lifecycle dates",
            
            "3. Date Extraction:",
            "   - Look for terms like: 'End of Support', 'End of Life', 'End of Service Life'",
            "   - For software: 'End of Security Support', 'End of Security Updates', 'End of Software Maintenance'",
            "   - Convert all dates to YYYY-MM-DD format",
            "   - If multiple dates exist, use the latest official announcement",
            "   - If no specific date is found, respond with 'None'",
            
            # "4. Reference Links:",
            # "   - Prioritize official manufacturer documentation",
            # "   - Verify that links are accessible and point to specific documents",
            # "   - Use permanent URLs rather than temporary or redirect links",
            # "   - If no official reference is available, use the most reliable alternative",
            
            "5. Data Validation:",
            "   - Ensure dates are logical and consistent with product lifecycle",
            "   - Cross-reference multiple sources when possible",
            "   - If conflicting dates are found, use the most recent official source",
            
            # "6. Manufacturer-Specific Handling:",
            # "   - For Cisco: Check cisco.com EOL notices",
            # # "   - For HP/HPE: Check support.hpe.com lifecycle pages",
            # # "   - For Dell: Check dell.com/support lifecycle information",
            # "   - For other manufacturers: Find their equivalent support pages"
        ],
        tools=[GoogleSearchTools(
            fixed_max_results=5,
        )],
        show_tool_calls=False
    )

    prompt = f'''Search and provide accurate the below dates for device: {device_name}

Return only the following details in JSON format:
- Last Date of Support for Hardware (HW)
- Last Date of Security Support for Software (SW)
- Include list of reference links for each date

If a date is not available, then use "None" as the date value.
# If no reference is found, use an empty list [].

The final output must be in this exact JSON format:
{{
  "Last Date of Support for HW": {{
    "date": YYYY-MM-DD, # if not available then return None.
    "reference": [list of strings]  # if not available then return [].
  }},
  "Last Date of Security Support for SW": {{
    "date": YYYY-MM-DD, # if not available then return None.
    "reference": [list of strings] # if not available then return [].
  }}
}}'''

    try:
        response: RunResponse = agent.run(prompt)
        json_str = extract_json_from_response(response.content)
        response_json = json.loads(json_str)
        return response_json

    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":

    # Example device name
    # device = "Cisco Catalyst 3850 Stack"
    device = "AIR-CT2504-K9"
    
    # Get the response
    result = get_device_support_dates(device)
    
    # Print the formatted JSON response
    print(json.dumps(result, indent=2))