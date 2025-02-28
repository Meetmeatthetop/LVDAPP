import subprocess
import sys

def update_dependencies():
    """Check for outdated packages and update them automatically."""
    try:
        print("🔍 Checking for outdated dependencies...\n")

        # Get list of outdated packages
        outdated_packages = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated", "--format=freeze"],
            capture_output=True, text=True
        ).stdout.splitlines()

        if not outdated_packages:
            print("✅ All dependencies are up to date!")
            return

        # Extract package names and update them
        for package in outdated_packages:
            pkg_name = package.split("==")[0].strip()
            print(f"⬆️ Updating {pkg_name}...")

            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", pkg_name])

        print("\n✅ All dependencies have been updated successfully!")

    except Exception as e:
        print(f"❌ Error updating dependencies: {e}")

if __name__ == "__main__":
    update_dependencies()
