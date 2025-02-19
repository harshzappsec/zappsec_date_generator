from openai import OpenAI
import json
import os

def get_device_support_dates(device_name):
    # Set your OpenAI API key
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    # Construct the prompt
    prompt = f'''Provide the below details as JSON for device: {device_name}, no extra information:  Last Date of Support for HW, Last Date of Security Support for SW with their reference links

The final output format as json would be 
{{
  "Last Date of Support for HW": {{
    "date": string
    "reference": string
  }},
  "Last Date of Security Support for SW": {{
    "date": string
    "reference": string
  }}
}}'''

    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={
              "type": "json_object"
            },
            temperature=0.3,
            max_completion_tokens=2048,
        )

        # Extract the response text
        response_text = response.choices[0].message.content

        # Parse the response as JSON
        response_json = json.loads(response_text)

        return response_json

    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Example device name
    device = "Cisco Catalyst 3850 Stack"
    
    # Get the response
    result = get_device_support_dates(device)
    
    # Print the formatted JSON response
    print(json.dumps(result, indent=2))