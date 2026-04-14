import json
import os
import toml

base_dir = '/Users/juanluisgrandi/AI/SiteCombustible1'
os.makedirs(os.path.join(base_dir, '.streamlit'), exist_ok=True)

try:
    with open(os.path.join(base_dir, 'secret_key.json'), 'r') as f:
        credentials = json.load(f)
    
    secrets = {
        "gsheets_creds": credentials
    }
    
    with open(os.path.join(base_dir, '.streamlit/secrets.toml'), 'w') as f:
        toml.dump(secrets, f)
        
    print("Secrets converted successfully")
except Exception as e:
    print(f"Error: {e}")
