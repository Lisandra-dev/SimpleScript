import argparse
import datetime
import sys
import shutil
from pathlib import Path
import os
import hashlib


def backup_folder(vault: Path, backup: Path):
    """
    Create a zip archive of a folder.
    Parameters
    ----------
    vault : Path
        Your vault folder.
    backup : Path
        Your backup folder.
    """
    zip_file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_file = Path(backup, zip_file)
    try:
        more_recent = max(backup.iterdir(), key=os.path.getctime)
        more_recent_md5 = hashlib.md5(open(more_recent, "rb").read()).hexdigest()
    except ValueError:
        more_recent_md5 = None
    tmp_vault = shutil.make_archive(str(zip_file), "zip", vault)
    tmp_vault_md5 = hashlib.md5(open(tmp_vault, "rb").read()).hexdigest()
    if more_recent_md5 == tmp_vault_md5:
        os.remove(tmp_vault)
        with open(Path(backup, "backup.log"), "a") as log:
            log.write(
                f"[{datetime.datetime.now()}] Archive not created, no changes detected.\r"
            )
    else:
        with open(Path(backup, "backup.log"), "a") as log:
            log.write(
                f"[{datetime.datetime.now()}] Archive created : {zip_file.name}\r"
            )


def delete_old_backups(folder: Path):
    """
    Delete your old backups.
    Also print a log in backup.log
    Parameters
    ----------
    folder : Path
        Your backup folder.
    """
    date_now = datetime.datetime.now()
    zip_removed = []
    for file in folder.iterdir():
        try:
            parse_date = datetime.datetime.strptime(file.name, "%Y-%m-%d_%H-%M-%S.zip")
            if (date_now - parse_date).days > 7:
                os.remove(file)
                zip_removed.append(file.name)
        except ValueError:
            pass
    if zip_removed:
        with open(Path(folder, "backup.log"), "a") as log:
            log.write(f"[{date_now}] Archive deleted : {', '.join(zip_removed)}\r")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a zip archive of your Obsidian vault in a specified location.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("vault", type=str, help="Your vault")
    parser.add_argument("backup", type=str, help="Your backup folder")
    args = parser.parse_args()
    vault = Path(args.vault)
    backup = Path(args.backup)
    if not vault.exists():
        print("Vault folder not found.")
        raise FileNotFoundError("Vault folder not found.")
    backup_folder(vault, backup)
    delete_old_backups(backup)
    sys.exit(0)
