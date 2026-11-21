import os

TEXT = "The light resting on your shoulders left its star before the first road was cut, and it is still arriving, slow as dust, in no hurry to be anywhere at all."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
