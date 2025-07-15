# pocketFlowProject
pocket flow question and answer chat boat using gemini
1. **Install Packages:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set API Key:**
   Set the environment variable for your Google Gemini API key.
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
   *(Replace `"your-api-key-here"` with your actual key)*

3. **Verify API Key (Optional):**
   Run a quick check using the utility script. If successful, it will print a short joke.
   ```bash
   python utils/call_llm.py
   ```
   *(Note: This requires a valid API key to be set.)*
