# PaperUpdater

A simple CLI tool to check for PaperMC server updates and apply them to your local server jar.

## Prerequisites

Before installing, ensure you have the following tools installed:

- **Git**: To clone the repository.
- **Poetry**: To manage dependencies.
  - You can install Poetry via `pipx install poetry` or the official installer.

## Installation

You can install PaperUpdater using the following command:

```bash
curl -sSL https://raw.githubusercontent.com/prismatic-beam/paperupdater/refs/heads/main/install.sh | bash
```

This will clone the repository to `~/paperupdater` and install the necessary dependencies using Poetry.

## Configuration

Before running the updater, you must configure the target directory for your Minecraft server.

1. Navigate to the installation directory:

   ```bash
   cd ~/paperupdater
   ```

2. Create a `.env` file defining the `PAPER_DIR` variable:
   ```env
   PAPER_DIR=/path/to/your/minecraft/server
   ```

## Usage

To run the updater, execute the `run.sh` script:

```bash
~/paperupdater/run.sh
```

### Options

- `-v`, `--verbose`: Enable verbose logging.
- `-r`, `--restore`: Restore the most recent backup (`.old` file) and exit.
- `-d <path>`, `--dir <path>`: Specify the server directory (overrides `PAPER_DIR` in `.env`).

## Optional: Add an Alias

To run the tool easily from anywhere, you can add an alias to your `.bashrc` (or `.zshrc`):

```bash
echo 'alias paperupdater="$HOME/paperupdater/run.sh"' >> ~/.bashrc
source ~/.bashrc
```
