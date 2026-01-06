# Research Note: Non-Human Identity (NHI) Sprawl & Governance
**ID:** RN-2025-002 | **Related Control:** [P1.T1.4_ADV], [P1.T2.2_ADV] | **Status:** Verified

## 🚨 The Threat Vector
**Machine-Identity Explosion:** As enterprises move to Agentic AI, the volume of Non-Human Identities (Service Accounts, API Keys, Bot Tokens) is growing at **100x the rate of human identities**.
*   **Attack:** "Secret Sprawl." Hardcoded credentials in agent code or logs are harvested by attackers to pivot laterally across cloud environments.
*   **Research Basis:** *GitGuardian State of Secrets Sprawl 2025*, *CISA NHI Guidance*.

## 🛡️ The AI SAFE² Solution
Standard IAM controls (designed for humans) fail at machine speed. AI SAFE² v2.1 introduces specific **NHI Governance Controls**:

### 1. Automated Enumeration [P1.T2.2_ADV]
Agents must be treated as "First-Class Citizens" in Identity Providers (IdP). We mandate automated discovery scripts to map every active agent to its specific permissions map.

### 2. Ephemeral Credentials [P5.T1.3_ADV]
Static long-lived API keys are prohibited for Tier 3 Agents.
*   **Implementation:** Use "Just-in-Time" (JIT) token generation via HashiCorp Vault or AWS STS. Keys exist only for the duration of the task.

### 3. Output Hygiene [P1.T1.4_ADV]
Real-time scanning of LLM output streams (using entropy detectors) to ensure an agent does not hallucinate or leak its own configuration secrets to a user.

## 📚 References
*   [GitGuardian: The Machine Identity Crisis](https://blog.gitguardian.com)
*   [CISA: Automated Security for Non-Human Identity](https://cisa.gov)
