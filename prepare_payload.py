import json, os
from pathlib import Path

log_text = Path("build_tail.log").read_text(errors="replace")

payload = {
    "run_id":   os.environ.get("GITHUB_RUN_ID", "0"),
    "repo":     os.environ.get("GITHUB_REPOSITORY", "unknown"),
    "commit":   os.environ.get("GITHUB_SHA", "unknown"),
    "branch":   os.environ.get("GITHUB_REF_NAME", "main"),
    "log_text": log_text
}

Path("payload.json").write_text(json.dumps(payload))
print(f"Payload written: {len(json.dumps(payload))} bytes")
