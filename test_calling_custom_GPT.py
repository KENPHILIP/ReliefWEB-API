import keyring
from openai import OpenAI

# Store your API key with this once
# import getpass; keyring.set_password(service_name="OPENAI_API_KEY", username="OPENAI_API_KEY", password=getpass.getpass())

api_key = keyring.get_password(service_name="OPENAI_API_KEY", username="OPENAI_API_KEY")

# Define a function to call the custom GPT model
# def call_custom_gpt(prompt, model="ReliefWeb Data Extractor", temperature=0.7, max_tokens=150):
#     response = openai.Completion.create(
#         model=model,
#         prompt=prompt,
#         temperature=temperature,
#         max_tokens=max_tokens
#     )
#     return response.choices[0].text.strip()

client = OpenAI(api_key=api_key, project="proj_qRxaDjDKSstrHX1hHZZ3XKXr")

# client.models.retrieve("gpt-3.5-turbo")

system_prompt = """Extract the following data in the following format from the input related to disaster relief.
    If there are multiple paragraphs, create a separate data record for each paragraph. Use numbers only for data fields.
    Keep the order of the fields as in the template.
    ```data = {
            "total_affected": "Data not available",
            "total_injured": "Data not available",
            "total_missing": "Data not available",
            "total_killed": "Data not available",
            "total_displaced": "Data not available",
            "economic_impact": "Data not available",
            "total_damaged_houses": "Data not available",
            "total_damaged_schools": "Data not available",
            "total_damaged_health_facilities": "Data not available"
        }```  Output only the results in the given format, with no additional commentary or explanation."""

# idx = 4
# print(disasters[idx]["fields"]["description"])
# prompt = disasters[idx]["fields"]["description"]

prompt = "In Rwanda, heavy rains and floods killed 14 people in Nyanza District, injured 27 in Burera District and damaged roads, bridges and 123 houses since 28 April and as of 2 May. Several hectares of rice and banana plantation in Ruhango District have been damaged, according to local authorities. Heavy rainfall, ranging between 40-50 mm, with thunderstorms is predicted to affect 17 districts across Northern, Western and Southern provinces between 30 April and 4 May, according to the Rwanda Meteorology Agency. Burera, Nyanza, Gakenke, and Ngororero districts received the highest amount of rainfall ranging from 84 to 105.2 mm between 30 April and 2 May. Impact such as severe widespread flooding to rivers, swamps and low-lying areas, landslides and damage to infrastructure are likely."
response = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
)
# print(response)
print(response.choices[0].message.content.strip())
