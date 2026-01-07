"""
AI SAFE² Quickstart: NHI Secret Hygiene Check [P1.T1.4_ADV]
Run this to see if your Agent configuration meets v2.1 standards.
"""
import re
import json

# Mock Agent Configuration (Simulating an insecure setup)
agent_config = {
    "agent_name": "Financial_Analyst_Bot",
    "model": "gpt-4-turbo",
    "env_vars": {
        "OPENAI_API_KEY": "sk-12345abcdef...",  # 🚨 VIOLATION: Hardcoded Key
        "DB_ACCESS": "read-write"
    }
}

def scan_for_secrets(config):
    print(f"🛡️ AI SAFE² v2.1 Compliance Scan: {config['agent_name']}")
    print("-" * 50)
    
    # Check 1: Hardcoded Secrets (Pillar 1)
    secret_pattern = r"(sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{20,})"
    config_str = json.dumps(config)
    
    if re.search(secret_pattern, config_str):
        print("❌ [FAIL] P1.T1.4: Hardcoded Secret detected in configuration.")
        print("   -> Action: Move keys to HashiCorp Vault or Environment Variables.")
    else:
        print("✅ [PASS] P1.T1.4: No hardcoded secrets found.")

if __name__ == "__main__":
    scan_for_secrets(agent_config)
