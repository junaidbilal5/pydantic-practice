import subprocess
import os


# ============================================================
# CONFIGURATION
# ============================================================

REPO_PATH = "/Users/bilal/Downloads/pydantic-practice"

GITHUB_REPO = "https://github.com/junaidbilal5/pydantic-practice.git"

BRANCH = "main"




# ============================================================
# HELPER FUNCTION
# ============================================================

def run_command(command, check=True):

    result = subprocess.run(
        command,
        cwd=REPO_PATH,
        text=True,
        capture_output=True
    )

    if check and result.returncode != 0:
        print("\n❌ Error:")
        print(result.stderr)
        exit(1)

    return result.stdout.strip()


# ============================================================
# CHECK LOCAL FOLDER
# ============================================================

if not os.path.exists(REPO_PATH):

    print("❌ Local repository folder does not exist:")
    print(REPO_PATH)

    exit(1)


print("\n📂 Repository:")
print(REPO_PATH)


# ============================================================
# FIRST-TIME GIT INITIALIZATION
# ============================================================

git_folder = os.path.join(REPO_PATH, ".git")


if not os.path.exists(git_folder):

    print("\n🆕 Git repository not initialized.")
    print("Initializing Git...")

    run_command(["git", "init"])

    print("✅ Git initialized.")

    # Set branch
    run_command(["git", "branch", "-M", BRANCH])

    print(f"✅ Branch set to {BRANCH}")

    # Add GitHub remote
    run_command([
        "git",
        "remote",
        "add",
        "origin",
        GITHUB_REPO
    ])

    print("✅ GitHub remote added.")


else:

    print("\n✅ Git repository already initialized.")


# ============================================================
# CHECK GITHUB REMOTE
# ============================================================

remote = run_command(
    ["git", "remote", "get-url", "origin"],
    check=False
)


if not remote:

    print("\n⚠️ GitHub remote is missing.")
    print("Adding GitHub remote...")

    run_command([
        "git",
        "remote",
        "add",
        "origin",
        GITHUB_REPO
    ])

    print("✅ GitHub remote added.")

else:

    print("\n🌐 Remote:")
    print(remote)


# ============================================================
# CHECK STATUS
# ============================================================

print("\n🔍 Checking Git status...\n")

status = run_command([
    "git",
    "status",
    "--short"
])


if not status:

    print("✅ No changes to commit.")
    exit(0)


print(status)


# ============================================================
# ASK USER FOR COMMIT MESSAGE
# ============================================================

print("\n" + "=" * 50)

commit_message = input(
    "💬 Enter your commit message: "
).strip()


# Don't allow empty commit message
if not commit_message:

    print("\n❌ Commit message cannot be empty.")
    exit(1)


# ============================================================
# ADD ALL CHANGES
# ============================================================

print("\n➕ Adding changes...")

run_command([
    "git",
    "add",
    "."
])


# ============================================================
# COMMIT
# ============================================================

print("\n📝 Creating commit...")

run_command([
    "git",
    "commit",
    "-m",
    commit_message
])

print("✅ Commit created.")


# ============================================================
# PUSH
# ============================================================

print("\n🚀 Pushing to GitHub...")

push_result = subprocess.run(
    ["git", "push", "-u", "origin", BRANCH],
    cwd=REPO_PATH,
    text=True,
    capture_output=True
)


if push_result.returncode != 0:

    print("\n❌ Push failed:")
    print(push_result.stderr)

    exit(1)


# ============================================================
# SUCCESS
# ============================================================

print("\n" + "=" * 50)
print("🎉 SUCCESS!")
print("=" * 50)

print(f"Commit: {commit_message}")
print(f"Branch: {BRANCH}")
print("Status: Pushed to GitHub ✅")