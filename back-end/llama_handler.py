import subprocess

def generate_report_from_symptoms(symptoms: str) -> str:
    prompt = f"You are a medical expert. Based on the following symptoms, generate a detailed personalized healthcare report with possible conditions, tests, medications, and follow-up recommendations.\n\nSymptoms: {symptoms}\n\nReport:"

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error generating report: {e.stderr}"
