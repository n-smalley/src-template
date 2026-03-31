#!/bin/bash
set -e

# Directory where this script lives (.setup_files)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parent directory (project root)
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Paths
VENV_DIR="$PROJECT_ROOT/.venv"
VENV_PYTHON="$VENV_DIR/bin/python"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

# Ensure python exists
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found on PATH"
    exit 1
fi

# Create venv if missing
if [ ! -f "$VENV_PYTHON" ]; then
    echo "CREATING VIRTUAL ENVIRONMENT @ $VENV_DIR"
    python3 -m venv "$VENV_DIR"
fi

# Activate venv (for user convenience only)
source "$VENV_DIR/bin/activate"

# Upgrade pip using venv python
"$VENV_PYTHON" -m pip install --upgrade pip

# Install dependencies
if [ -f "$REQUIREMENTS" ]; then
    echo "INSTALLING DEPENDENCIES $REQUIREMENTS"
    "$VENV_PYTHON" -m pip install -r "$REQUIREMENTS" \
        --trusted-host pypi.org \
        --trusted-host pypi.python.org \
        --trusted-host files.pythonhosted.org \
        --default-timeout=1000
else
    echo "ERROR: requirements.txt not found"
    exit 1
fi

echo ""
echo "Setup complete."
echo "Python in use:"
"$VENV_PYTHON" --version