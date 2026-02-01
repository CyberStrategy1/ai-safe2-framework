# Ishi + OpenClaw Integration Guide (Windows 11)

**Complete setup: Command center (Ishi) + Execution arm (OpenClaw)**

**Your System:** Windows 11 - Perfect for this setup

**Time:** 2 hours total

---

## ARCHITECTURE

```
Windows 11 Desktop
├─ Ishi (Native .exe)
│  ├─ Local file operations
│  ├─ Strategic planning
│  ├─ AgenticFlow orchestration
│  └─ Delegates to OpenClaw
│
├─ WSL2 Ubuntu 22.04
│  ├─ OpenClaw (Node.js server)
│  ├─ AI SAFE² Gateway (Python)
│  └─ 24/7 autonomous operations
│
└─ AI SAFE² Security Layer
   ├─ Ishi memory protocol
   ├─ OpenClaw memory protocol
   ├─ Central audit logging
   └─ Cross-agent validation
```

---

## PHASE 1: ENVIRONMENT SETUP (30 min)

### Install WSL2

```powershell
# Run PowerShell as Administrator
wsl --install
# Restart computer when prompted
```

After restart:
```powershell
# Install Ubuntu 22.04
wsl --install -d Ubuntu-22.04
# Set username: openclaw
# Set password: [secure password]
```

### Update Ubuntu
```bash
# In WSL2 terminal
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip nodejs npm curl git
```

---

## PHASE 2: INSTALL ISHI (15 min)

### Download & Install
```powershell
# Download Ishi for Windows
Invoke-WebRequest -Uri "https://ishi.so/download?platform=win-x64" -OutFile "IshiSetup.exe"

# Install
.\IshiSetup.exe
# Follow prompts, accept defaults
```

### Initial Configuration
```
1. Launch Ishi from Start menu
2. Run: /connect
3. Select provider:
   - Option A: Gemini (free, 1,500 req/day)
   - Option B: Ishi Intent Engine (paid, better)
4. Add API key
5. Test: "Hello"
```

---

## PHASE 3: INSTALL OPENCLAW (20 min)

### In WSL2 Ubuntu

```bash
# Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# Verify
openclaw --version
```

### Configure OpenClaw
```bash
mkdir -p ~/.openclaw
nano ~/.openclaw/openclaw.json
```

Add:
```json
{
  "anthropic": {
    "api_key": "YOUR_KEY"
  },
  "gateway": {
    "bind": "127.0.0.1",
    "port": 18789
  },
  "tools": {
    "exec": {"enabled": false},
    "browser": {"enabled": false}
  }
}
```

Save and start:
```bash
openclaw gateway --bind 127.0.0.1
```

---

## PHASE 4: DEPLOY AI SAFE² FOR ISHI (20 min)

### Memory Protocol
```powershell
# Download
cd $env:APPDATA\ishi\memories\
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/CyberStrategyInstitute/ai-safe2-framework/main/examples/ishi/ishi_memory.md" -OutFile "ishi_memory.md"

# Restart Ishi
Stop-Process -Name "ishi" -Force
Start-Process "ishi"
```

### Scanner
```powershell
cd $env:USERPROFILE\Downloads
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/CyberStrategyInstitute/ai-safe2-framework/main/examples/ishi/ishi-scanner.py" -OutFile "ishi-scanner.py"

python ishi-scanner.py
# Fix any CRITICAL/HIGH findings
```

### Configure
```
In Ishi:
/config permissions → Level 2 (Associate)
/config tokens → Enable tracking
/config ghost_files → Disable auto-commit
```

---

## PHASE 5: DEPLOY AI SAFE² FOR OPENCLAW (20 min)

### In WSL2 Ubuntu

```bash
cd ~/.openclaw
git clone https://github.com/CyberStrategyInstitute/ai-safe2-framework.git
cd ai-safe2-framework/examples/openclaw/

# Memory protocol
cp openclaw_memory.md ~/.openclaw/memories/

# Scanner
python3 scanner.py --path ~/.openclaw
# Fix findings

# Gateway
cd gateway/
export ANTHROPIC_API_KEY="sk-ant-..."
./start.sh
```

---

## PHASE 6: CONNECT ISHI ↔ OPENCLAW (15 min)

### Configure Ishi to Delegate to OpenClaw

```powershell
# Edit Ishi config
$configPath = "$env:APPDATA\ishi\config.json"
$config = Get-Content $configPath | ConvertFrom-Json

# Add OpenClaw integration
$config | Add-Member -NotePropertyName "integrations" -NotePropertyValue @{} -Force
$config.integrations | Add-Member -NotePropertyName "openclaw" -NotePropertyValue @{
    enabled = $true
    endpoint = "http://localhost:18789"
    require_approval = $true
    health_check = $true
    max_timeout_seconds = 300
} -Force

$config | ConvertTo-Json -Depth 10 | Out-File $configPath -Encoding UTF8
```

### Test Connection

```
In Ishi: "Test OpenClaw connection"
Expected: "✓ OpenClaw responding"
```

---

## PHASE 7: REAL-WORLD USE CASES

### Personal: Travel Concierge (15 min setup)

**The Goal:** Monitor flight prices 24/7, get alerted when deals appear

**Ishi does:**
- Manages `Travel_Plan.md` locally
- Drafts packing lists based on weather data
- Creates ghost booking confirmations

**OpenClaw does:**
- Monitors SFO→NRT route pricing overnight (Browser-use)
- Checks hotel availability
- Scrapes seat maps to avoid "bad seats"

**The Integration Flow:**
1. **Setup:** "OpenClaw, monitor SFO to NRT for June. Alert if price <$900"
2. **Action:** OpenClaw finds deal at 3 AM
3. **Alert:** Ishi creates ghost booking draft + phone notification
4. **Approval:** You wake up, review in Ishi, click "Execute Booking"

**Implementation:**
```bash
# In OpenClaw (WSL2)
# Install browser-use skill
npm install @browser-use/core

# Configure monitoring
openclaw skill add flight-monitor \
  --route "SFO-NRT" \
  --max-price 900 \
  --check-interval "6h" \
  --notify-via ishi
```

```
# In Ishi
"Create Travel_Plan.md with:
- Departure: June 15, 2026
- Route: SFO → NRT
- Budget: $900
- Notify me of deals via ghost file"
```

**AI SAFE² Protection:**
- ✅ Booking requires approval (no auto-purchase)
- ✅ Price verified against ghost file preview
- ✅ Credit card never stored in OpenClaw

---

### Personal: Health & Bio-Optimization (20 min setup)

**The Goal:** Track health trends, get supplement recommendations

**Ishi does:**
- Analyzes Apple Health CSV exports locally
- Creates visual trend dashboards
- Maintains `Health_Log.xlsx`

**OpenClaw does:**
- Monitors Oura/Whoop APIs 24/7
- Researches supplement studies when trends flag
- Checks pharmacy stock for specific items

**The Integration Flow:**
1. **Setup:** "If recovery <70 for 3 days, research magnesium dosage"
2. **Detection:** Ishi detects trend in local data
3. **Research:** OpenClaw scrapes latest studies
4. **Draft:** Ishi creates ghost shopping list
5. **Approval:** You review research before adding to grocery list

**Implementation:**
```
# In Ishi
"Monitor my Health_Exports folder.
If recovery trend drops:
1. Analyze last 7 days locally
2. Ask OpenClaw to research supplements
3. Draft shopping list in Life_OS folder
4. Wait for my approval"
```

```bash
# In OpenClaw
openclaw skill add health-monitor \
  --api oura \
  --metric recovery \
  --threshold 70 \
  --research-topics "magnesium,sleep-optimization"
```

**Privacy Note:** Raw health data NEVER leaves Ishi (local only). OpenClaw only sees anonymized trends.

---

### Business: CRM Lead Nurturing (30 min setup)

**The Goal:** Auto-detect trigger events, draft personalized outreach

**Ishi does:**
- Manages `Leads_Tracker.xlsx` locally
- Drafts personalized emails
- Maintains relationship context

**OpenClaw does:**
- Scrapes LinkedIn/Google News 24/7
- Detects trigger events (funding, job changes, news mentions)
- Enriches lead profiles

**The Integration Flow:**
1. **Setup:** "Monitor companies in Leads file for news mentions"
2. **Detection:** OpenClaw finds "Acme Corp raised $50M"
3. **Enrichment:** OpenClaw summarizes article + extracts key points
4. **Draft:** Ishi creates ghost "Congrats" email
5. **Approval:** You tweak draft, hit send

**Implementation:**
```
# In Ishi
"Maintain Leads_Tracker.xlsx.
For each company:
1. Ask OpenClaw to monitor news
2. When trigger detected, draft email
3. Include: personalized hook, relevant context
4. Create as ghost file for my review"
```

```bash
# In OpenClaw
openclaw skill add lead-monitor \
  --source "google-news,linkedin" \
  --triggers "funding,acquisition,executive-change" \
  --notify ishi-drafts
```

**Result:** First-mover advantage on outreach, 24/7 monitoring

---

### Business: Content Repurposing Engine (25 min setup)

**The Goal:** Turn YouTube videos into multi-platform content automatically

**Ishi does:**
- Processes raw `.mp4` files locally (privacy)
- Segments transcripts using local LLM
- Creates `Content_Package` ghost files

**OpenClaw does:**
- Monitors X/YouTube for trending hooks (24/7)
- Schedules finalized posts overnight
- Tracks engagement metrics

**The Integration Flow:**
1. **Setup:** "When .mp4 added to Raw_Video, segment transcript"
2. **Processing:** Ishi extracts timestamps, key quotes locally
3. **Context:** OpenClaw provides 3 trending hooks from X
4. **Package:** Ishi creates ghost content bundle
5. **Approval:** You approve, OpenClaw pushes to Buffer/Hypefury

**Implementation:**
```
# In Ishi
"Watch /Raw_Video folder.
For each .mp4:
1. Extract transcript locally
2. Identify 5 key moments
3. Ask OpenClaw for trending hooks
4. Create content package as ghost file"
```

```bash
# In OpenClaw
openclaw skill add trend-monitor \
  --platforms "x,youtube" \
  --topics "AI,automation,productivity" \
  --alert-threshold "outlier-performance"

openclaw skill add content-scheduler \
  --buffer-api "$BUFFER_KEY" \
  --schedule "optimal-times"
```

---

### Business: Overnight DevSecOps (20 min setup)

**The Goal:** Security audits and dependency updates while you sleep

**Ishi does:**
- Manages local Git repo
- Reviews PRs with diff-viewer
- Creates ghost patch files

**OpenClaw does:**
- Runs security scans at 11 PM (WSL2 Docker)
- Tests dependency updates
- Creates PRs with vulnerability reports

**The Integration Flow:**
1. **Setup:** "Every night at 11 PM, run security scan on /src"
2. **Scan:** OpenClaw finds outdated library
3. **Patch:** OpenClaw tests update, creates PR
4. **Report:** Ishi presents ghost vulnerability report
5. **Approval:** You review diff, click "Merge"

**Implementation:**
```bash
# In OpenClaw (WSL2)
# Add cron job
crontab -e
# Add: 0 23 * * * openclaw task security-audit --repo /workspace/src

openclaw skill add security-audit \
  --tools "snyk,npm-audit,trivy" \
  --create-pr-on-fix \
  --notify ishi
```

```
# In Ishi
"Monitor OpenClaw security reports.
For each vulnerability:
1. Show me the diff
2. Explain the risk
3. Create ghost patch for review
4. Don't merge without approval"
```

**Result:** Wake up to tested, ready-to-merge security fixes

---

## TESTING (20 min)

### Test 1: Ishi Local Operations
```
In Ishi: "Organize my Downloads by file type"
Expected: Ghost files, preview, approval required
```

### Test 2: OpenClaw 24/7 Monitoring
```bash
# In WSL2
openclaw gateway --bind 127.0.0.1

# Send test message via configured channel
Expected: OpenClaw responds, logs to audit trail
```

### Test 3: Ishi → OpenClaw Delegation
```
In Ishi: "Ask OpenClaw to check the weather"
Expected:
1. Ishi requests approval
2. You approve
3. Ishi sends to OpenClaw
4. OpenClaw executes
5. Ishi shows result
```

### Test 4: AI SAFE² Blocking
```
In Ishi: "Delete all files in Documents"
Expected: BLOCKED by memory protocol, violation logged
```

---

## ONGOING OPERATIONS

### Daily (Automatic)
- Ishi tracks token usage
- OpenClaw logs all actions
- Both systems monitor violations

### Weekly (5 min)
```powershell
# Scan Ishi
python ishi-scanner.py

# Scan OpenClaw (in WSL2)
wsl -d Ubuntu -- python3 ~/.openclaw/ai-safe2-framework/examples/openclaw/scanner.py --path ~/.openclaw
```

### Monthly (15 min)
- Review audit logs
- Purge old trash/snapshots
- Update memory protocols if new version

---

## FREE TIER OPERATION

### Token Budget Strategy

**Gemini (free):** 1,500 req/day
- Use for: Ishi file operations, analysis
- Cost: $0

**OpenClaw via Gemini:**
- Same limit, shared with Ishi
- Monitor with: `cat ~/.openclaw/ai-safe2-framework/examples/openclaw/gateway/gateway_audit.log`

**Combined Daily Budget:**
```
Ishi: 1,000 requests
OpenClaw: 500 requests
Total: 1,500 requests (at limit)
```

**If exceeded:**
1. Auto-switch to OpenRouter free models
2. OR wait until tomorrow (resets 12 AM PT)
3. OR upgrade to Ishi Intent Engine (1M tokens/month)

---

## TROUBLESHOOTING

### Ishi Can't Reach OpenClaw

**Check:**
```powershell
# OpenClaw running?
wsl -d Ubuntu -- ps aux | Select-String openclaw

# Port accessible?
Test-NetConnection -ComputerName localhost -Port 18789
```

**Fix:**
```bash
# In WSL2, restart OpenClaw
pkill -f openclaw
openclaw gateway --bind 127.0.0.1
```

### WSL2 Network Issues

**Symptom:** Windows can't reach WSL2 services

**Fix:**
```powershell
# Restart WSL2
wsl --shutdown
wsl -d Ubuntu

# Get WSL2 IP
wsl -d Ubuntu hostname -I
# Update Ishi config with this IP if needed
```

---

## PRODUCTION HARDENING

### Lock Down WSL2
```bash
# In WSL2
sudo ufw enable
sudo ufw allow from 127.0.0.1
sudo ufw allow from 172.16.0.0/12  # WSL2 subnet
sudo ufw default deny incoming
```

### Windows Firewall
```powershell
# Block WSL2 external access (allows localhost)
New-NetFirewallRule -DisplayName "Block WSL2 External" -Direction Inbound -InterfaceAlias "vEthernet (WSL)" -Action Block
```

### Schedule Scans
```powershell
# Ishi scan (weekly)
$action = New-ScheduledTaskAction -Execute "python" -Argument "$env:USERPROFILE\Downloads\ishi-scanner.py"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9AM
Register-ScheduledTask -TaskName "IshiSecurityScan" -Action $action -Trigger $trigger
```

---

## SUMMARY

**What you built:**
- ✅ Ishi: Local-first AI (privacy, safety, ghost files)
- ✅ OpenClaw: 24/7 server agent (adaptive learning, multi-channel)
- ✅ AI SAFE²: Security layer protecting both
- ✅ Integration: Ishi delegates to OpenClaw when needed
- ✅ Free tier: Works with Gemini (1,500 req/day)
- ✅ Token tracking: Prevents overages
- ✅ Audit logging: Complete visibility

**Total cost:** $0/month (free tier) or $30/month (Ishi Intent Engine for unlimited)

**Time to deploy:** 2 hours

**Maintenance:** 5 minutes/week

---

**Document Version:** 2.1  
**Platform:** Windows 11  
**Tested On:** i5, 16GB RAM
