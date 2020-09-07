def start():
    import subprocess
    subprocess.run("/entrypoint.sh")
    subprocess.run("/start.sh")


def main():
    start()


if __name__ == "__main__":
    main()
