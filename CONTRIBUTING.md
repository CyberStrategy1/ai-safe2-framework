# Contributing to AI SAFE²

Thank you for your interest in hardening the AI ecosystem. We welcome contributions from security researchers, AI engineers, and GRC experts.

## 📋 How to Contribute

### 1. Reporting Gaps (The "Issues" Tab)
Do not modify the README directly for suggestions.
*   **Found a missing threat?** Open an Issue tagged `[Gap Analysis]`.
*   **Found a typo?** Open an Issue tagged `[Editorial]`.
*   **Proposing a new Control?** Open an Issue tagged `[New Control]`.

### 2. Proposing Changes (Pull Requests)
If you are submitting a Pull Request (PR), please adhere to the **Control ID Syntax**:
*   **Format:** `P{Pillar}.T{Topic}.{ID}` (e.g., `P1.T1.5`).
*   **Advanced Controls:** Must append `_ADV` (e.g., `P1.T1.2_ADV`).
*   **Requirement:** Every new control must include a `technical_check` and a suggested tool.

## 📝 Style Guide
*   **Tone:** Clinical, operational, and imperative. (e.g., "Implement X," not "You should try X").
*   **Mappings:** If adding a control, you *must* cite the mapping (NIST, MITRE, ISO) if applicable.

## 🤝 Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## ⚖️ License
By contributing, you agree that your contributions will be licensed under the project's **Dual License** (CC-BY-SA 4.0 for text, MIT for code).
