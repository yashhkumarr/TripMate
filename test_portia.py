import os
from dotenv import load_dotenv
from portia import Config, LLMProvider, Portia, StorageClass

print("--- Starting Agent Test ---")

# 1. Load the .env file
print("1. Loading .env file...")
load_dotenv()
print("   File loaded.")

# 2. Read the API Keys
print("\n2. Reading API keys from environment...")
portia_key = os.getenv("PORTIA_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

if portia_key:
    print("   ✅ PORTIA_API_KEY found.")
else:
    print("   ❌ FAILED: PORTIA_API_KEY not found.")

if google_key:
    print("   ✅ GOOGLE_API_KEY found.")
else:
    print("   ❌ FAILED: GOOGLE_API_KEY not found.")

# 3. Try to Initialize the Agent
if portia_key and google_key:
    print("\n3. Attempting to initialize Portia agent...")
    try:
        my_config = Config.from_default(
            llm_provider=LLMProvider.GOOGLE,
            default_model="gemini-1.5-pro",
            storage_class=StorageClass.CLOUD
        )

        portia_agent = Portia(config=my_config)
        
        print("\n-----------------------------------------")
        print("✅✅✅ SUCCESS! Agent initialized correctly.")
        print("-----------------------------------------")

    except Exception as e:
        print("\n----------------------------------------------------")
        print(f"❌❌❌ FAILED: Could not initialize agent.")
        print(f"ERROR DETAILS: {e}")
        print("----------------------------------------------------")
else:
    print("\nSkipping agent initialization because API keys are missing.")

print("\n--- Test Complete ---")