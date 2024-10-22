# Install UV per UV website instructions
curl -LsSf https://astral.sh/uv/install.sh | sh
# Make UV available
source $HOME/.cargo/env
# UV to set up a normal Python environment
uv venv
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
source .venv/bin/activate