"""
DevOps Assistant Agent — API Integration Example

Requires:
    pip install google-cloud-dialogflow-cx==1.35.0

Set environment variable:
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
"""

from google.cloud.dialogflowcx_v3 import AgentsClient, SessionsClient, TextInput, QueryInput

PROJECT_ID = "zoneloop-automation"
LOCATION = "us-west1"
AGENT_ID = "1778502370266"
SESSION_ID = "test-session-001"


def query_agent(text: str) -> str:
    session_path = f"projects/{PROJECT_ID}/locations/{LOCATION}/agents/{AGENT_ID}/sessions/{SESSION_ID}"
    client = SessionsClient(client_options={"api_endpoint": f"{LOCATION}-dialogflow.googleapis.com"})

    response = client.detect_intent(
        request={
            "session": session_path,
            "query_input": QueryInput(
                text=TextInput(text=text),
                language_code="th",
            ),
        }
    )

    return response.query_result.response_messages[0].text.text[0]


if __name__ == "__main__":
    answer = query_agent("อธิบาย architecture ของ LLM Gateway")
    print(answer)
