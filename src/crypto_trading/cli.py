import argparse
from .demo import run_demo

def main():
    parser = argparse.ArgumentParser(description="Crypto Trading Information System (paper-only)")
    parser.add_argument("command", choices=["demo"], help="Command to run")
    args = parser.parse_args()
    if args.command == "demo":
        run_demo()
