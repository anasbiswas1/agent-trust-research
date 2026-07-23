"""Central config. Import paths from here; never hardcode."""
from pathlib import Path

PROJECT   = "AGENTTRUST"
REPO_NAME = "agent-trust-research"
GH_USER   = "anasbiswas1"

DRIVE_ROOT = Path("/content/drive/MyDrive") / f"{PROJECT}_Research"
REPO_DIR   = DRIVE_ROOT / REPO_NAME

NOTEBOOKS = REPO_DIR / "notebooks"
SRC       = REPO_DIR / "src"
REPORTS   = REPO_DIR / "reports"
FIGURES   = REPO_DIR / "figures"
DATA      = REPO_DIR / "data"
EXTERNAL  = REPO_DIR / "external"

# third-party artifacts
ADI_REPO        = EXTERNAL / "adi"
AGENTDOJO_REPO  = EXTERNAL / "agentdojo"
PFI_REPO        = EXTERNAL / "pfi"

# ADI paper reference values (arXiv:2607.05120) for inventory checks
ADI_EXPECTED = {
    "user_tasks": 96,
    "adi_attacks": 108,
    "suites": {
        "workspace": {"user_tasks": 39, "adi_attacks": 55},
        "slack":     {"user_tasks": 21, "adi_attacks": 16},
        "banking":   {"user_tasks": 16, "adi_attacks": 9},
        "travel":    {"user_tasks": 20, "adi_attacks": 28},
    },
    "instruction_injection_attacks": 935,
    "tool_response_format": "json",
}

def ensure_dirs():
    for p in (NOTEBOOKS, SRC, REPORTS, FIGURES, DATA, EXTERNAL):
        p.mkdir(parents=True, exist_ok=True)
