# AES-ECB Streamlit Demo

This repository contains a Streamlit multi-page application that demonstrates AES encryption
using ECB (Electronic Code Book) mode. Each section (Introduction, Objective, Theory, Simulation,
Procedure, Conclusion) is provided as a separate page under the `pages/` folder.

Files created:
- `Home.py` — Main landing page
- `common.py` — Shared helpers (CSS injection, AES encrypt/decrypt functions)
- `pages/Introduction.py`, `pages/Objective.py`, `pages/Theory.py`, `pages/Simulation.py`, `pages/Procedure.py`, `pages/Conclusion.py` — Section pages

Requirements:
- Python 3.8+
- See `requirements.txt` for pinned packages

Quick start (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run Home.py
```

Notes:
- If PowerShell execution policy blocks activation, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` as admin or use `cmd.exe` to activate the venv.
- The app uses `pycryptodome` for AES operations.
